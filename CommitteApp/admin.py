from django.contrib import admin
from CommitteApp.models import *
# Register your models here.
@admin.register(CentralYear)
class CentralYearAdmin(admin.ModelAdmin):
    list_display = ['yearname']

@admin.register(CentralMember)
class CentralMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position','session', 'phone']
    list_editable = ['session', 'position']
    list_filter = ['session']

@admin.register(BranchCategory)
class BranchCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(BranchYear)
class BranchYearAdmin(admin.ModelAdmin):
    list_display = ['branchyear', 'branches']
    list_filter = ['branches']

@admin.register(BranchMember)
class BranchMemberAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'position', 'branch_year']
    list_filter = ['branch_year']


@admin.register(BranchName)
class BranchNameAdmin(admin.ModelAdmin):
    list_display = ['branchname']
    list_filter = ['branch_category']