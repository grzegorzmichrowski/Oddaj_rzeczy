from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from oddaj_rz.forms import LoginForm


class LandingPageView(View):

    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                if user.is_staff:
                    return redirect('admin/')
                return redirect('landing_page')
        return render(request, 'login.html')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('landing_page')


class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get("login")
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('password2')
        users = User.objects.all()
        usernames = []
        emails = []
        for i in users:
            emails.append(i.email)
            usernames.append(i.username)
        if name and surname and username and email and password and confirmPassword and password == confirmPassword:
            if username in usernames:
                text = 'Podany użytkownik już istnieje'
                return render(request, 'register.html', {"text": text})
            elif email in emails:
                text = 'Podany email już istnieje'
                return render(request, 'register.html', {"text": text})
            else:
                User.objects.create_user(first_name=name,
                                         last_name=surname,
                                         username=username,
                                         email=email,
                                         password=password,
                                         )
                return redirect('login')
        text = 'Hasła niezgodne'
        return render(request, 'register.html', {"text": text})