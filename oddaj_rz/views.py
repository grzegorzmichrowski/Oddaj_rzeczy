from django.contrib.auth import authenticate, login, logout
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
            user = authenticate(username=form.cleaned_data['email'].value(),
                                password=form.cleaned_data['password'].value())
            if user:
                login(request, user)
                return redirect('landing_page')
        return render(request, 'login.html')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('landing_page')
