from django.contrib import admin
from Contact_app.models import *
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone','email', 'status']
    list_editable = ['status']
    list_filter = ['status']
    search_fields = ('name', 'phone')
    readonly_fields =('name', 'phone', 'email', 'message')
