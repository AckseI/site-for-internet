from django import forms
from django.forms import ModelForm
from .models import Articles

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'
        labels = {
            'title': 'Название статьи',
            'text': 'Текст статьи',
        }
        widjets = {
            'title': forms.CharField(attrs={}),
            'comment': forms.Te
        }