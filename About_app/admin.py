from django.contrib import admin

# Register your models here.
from About_app.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
   

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']
