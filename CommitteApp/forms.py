from CommitteApp.models import *
from django import forms
class CentralForm(forms.ModelForm):
    class Meta:
        model = CentralYear
        fields = '__all__'

class CentralMemberForm(forms.ModelForm):
    class Meta:
        model = CentralMember
        fields = '__all__'
        exclude = ['session',]

class BranchCategoryForm(forms.ModelForm):
    class Meta:
        model = BranchCategory
        fields = '__all__'

class BranchNameForm(forms.ModelForm):
    class Meta:
        model = BranchName
        fields = ['branchname']


class BranchYearForm(forms.ModelForm):
    class Meta:
        model = BranchYear
        fields = ['branchyear']

class MemberAddForm(forms.ModelForm):
    class Meta:
        model = BranchMember
        fields = ('photo', 'name', 'position', 'gender', 'University', 'blood_group','phone', 'current_enroll',
                   'facebook', 'instagram', 'twitter', 'linkdin',)

class CoordinatorForm(forms.ModelForm):
    class Meta:
        model = Coordinator
        fields = '__all__'