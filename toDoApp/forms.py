from django.forms import ModelForm
from .models import Todo

class TaskModel(ModelForm):
    class Meta:
        model = Todo
        fields = ['title']
