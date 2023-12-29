from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # * Formulario proporcionado por Django
# Create your views here.

def helloWorld(request):
    return render(request, 'signup.html', {
        'form' : UserCreationForm(),
    })