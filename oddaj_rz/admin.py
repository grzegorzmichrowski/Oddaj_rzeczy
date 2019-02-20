from django.contrib import admin

# Register your models here.
from oddaj_rz.models import Institution, Location, Category, Target

admin.site.register(Institution)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Target)