from django.contrib import admin
from Profile_app.models import *
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [ 'user','fathername', 'mothername', 'current_enroll']
    search_fields = ('name', 'current_enroll')
    list_filter =['current_enroll']
    # prepopulated_fields = {'slug': ('user',)}
    readonly_fields =('user',
             'photo',
            'university',
            'School',
            'college',
            'gender',
            'status',
            'fathername',
            'mothername',
            'deparment',
            'birthday',
            'current_enroll',
            'religion',
            'Class',
            'Village',
            'thana',
            'phone',
            'district',
            'current_city',
            'local_city',
            'facebook',
            'twitter',
            'instagram',
            'linkdin')

admin.site.register(StudentCategory)

