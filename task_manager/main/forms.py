from .models import Task
from django.forms import ModelForm, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
