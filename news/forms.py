from django.forms import ModelForm, TextInput, Textarea
from .models import Articles

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "text": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Текст статьи"
            })
        }