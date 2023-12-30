from django.forms import ModelForm
from .models import Task

# * Otra manera de crear un Form, visitar: https://github.com/JeanGC970520/mysite/blob/main/myapp/forms.py 
# * para visualizar un segundo metodo de creacion de un Form
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'important',
        ]
