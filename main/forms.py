from .models import Link, Theme
from django.forms import ModelForm, TextInput, ModelChoiceField


class VideoForm(ModelForm):
    class Meta:
        model = Link
        fields = ['button_text', 'link_address', 'theme_id']
        theme_id = ModelChoiceField(Theme.objects.all())
        widgets = {
            "button_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Добавьте название'
            }),
            'link_address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Добавьте ссылку'
            })
        }
