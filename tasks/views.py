from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # * Formulario proporcionado por Django
from django.contrib.auth.models import User # * Modelo proporcionado ya por Django. Aunque podemos hacer los nuestros
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form' : UserCreationForm(),
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                # Creando User
                user =User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1']
                )
                # Guardando User en DB
                user.save()
                return redirect('tasks') # Redireccionando a la ruta con nombre 'tasks'
            except Exception as e:
                print(e)
                return render(request, 'signup.html', {
                    'form' : UserCreationForm(),
                    'error' : 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form' : UserCreationForm(),
            'error' : 'Password do not match'
        })
    
def tasks(request):
    return render(request, 'tasks.html')