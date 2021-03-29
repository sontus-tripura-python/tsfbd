from django import forms
from News.models import *
from django.forms.widgets import NumberInput , Textarea, Textarea
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'image', 'news_description', 'posted_name', 'facebook']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': Textarea(attrs={ 'cols':40, 'rows':3}),
        }
