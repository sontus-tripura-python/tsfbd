.from django import forms
from Notice.models import *
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'posted_name', 'facebook']