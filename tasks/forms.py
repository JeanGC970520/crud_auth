from django import forms
from .models import Task

# * Otra manera de crear un Form, visitar: https://github.com/JeanGC970520/mysite/blob/main/myapp/forms.py 
# * para visualizar un segundo metodo de creacion de un Form
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'important',
        ]
        # * Con la propiedad de clase 'widgets' podemos indicar que tipo de entrada sera cada field.
        # * Ademas de asignarle clases para uso ya sea con CSS o Bootstrap como lo es en este caso.
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Write a title'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Write a description'}),
            'important' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
        }
