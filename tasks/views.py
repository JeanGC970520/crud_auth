from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # * Formularios proporcionado por Django
from django.contrib.auth.models import User # * Modelo proporcionado ya por Django. Aunque podemos hacer los nuestros
# * login() crea una cookie para notificar que el usario ya fue autenticado
# * logout() elimina la persistencia del User que haya creado el login()
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        # UserCreationForm() sirve para cuando se quiera crear un nuevo User
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
                # Conserve una identificación de usuario y un backend en la solicitud.
                # De esta manera, un usuario no tiene que volver a autenticarse en cada solicitud.
                login(request, user)
                return redirect('tasks') # Redireccionando a la ruta con nombre 'tasks'
            except IntegrityError:
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

def createTask(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form' : TaskForm(),
        })
    else: 
        print(request.POST)
        return render(request, 'create_task.html', {
            'form' : TaskForm(),
        })

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        # AuthenticationForm() para comprobar si el usuario existe
        return render(request, 'signin.html', {
            'form' : AuthenticationForm(),
        })
    else:
        # Verifica si las credenciale son validas en la DB
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is None:
            return render(request, 'signin.html', {
                'form' : AuthenticationForm(),
                'error' : 'Username or password is incorrect'
            })
        # Si el User ya es valido se hace persistente la sesion
        login(request, user)
        return redirect('tasks')
