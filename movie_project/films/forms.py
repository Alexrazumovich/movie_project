from .models import Films_post
from django.forms import ModelForm,TextInput,DateTimeInput,Textarea

class Films_postForm(ModelForm):
    class Meta:
        model = Films_post
        fields = ['title', 'short_description', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв'}),

        }
