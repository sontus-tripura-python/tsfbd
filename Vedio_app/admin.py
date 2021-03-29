from django.contrib import admin

# Register your models here.
from Vedio_app.models import *
@admin.register(Vedio)
class VedioAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}