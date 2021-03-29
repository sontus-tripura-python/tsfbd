from django import forms
from Vedio_app.models import *
from django.forms.widgets import NumberInput , Textarea, Textarea
class CommentForm(forms.ModelForm):
    class Meta:
        model = VedioComment
        fields = ['name','comment']
        widgets = {
            'comment': Textarea(attrs={ 'cols':40, 'rows':3}),
        }
