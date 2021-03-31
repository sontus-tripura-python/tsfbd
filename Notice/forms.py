.from django import forms
from Notice.models import *
class NoticeBoardForm(forms.ModelForm):
    class Meta:
        model = NoticeBoard
        fields = ['title', 'description', 'posted_name', 'facebook']