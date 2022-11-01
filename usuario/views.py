from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import form_cliente
from .models import Panel_Cliente

import usuario

# Create your views here.


def Home(request):

    return render(request, 'home.html')


def Logueo(request):

    if request.method == 'GET':
        print('Enviando Formulario')

        return render(request, 'logueo.html', {
            'form_cliente': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                login(request, usuario)  # ACA CREO LA COOKIE EL LOGIN
                # ACA REDIRECCIONO SI EL LOGUEO FUE CORRECTO
                return redirect('ingreso')
            except IntegrityError:  # ACA CHEQUEO EXCEPCIONES DESDE LA BASE DE DATOS
                return render(request, 'logueo.html', {
                    'form_cliente': UserCreationForm,
                    'error': 'El Usuario Ya Existe'
                })

        return render(request, 'logueo.html', {
            'form_cliente': UserCreationForm,
            'error': 'Las Constraseñas No Coinciden Por Favor Verifique Los Datos'
        })


def Ingreso(request):
    tareas= Panel_Cliente.objects.filter(usuario=request.user) # aca filtro por alumnos de profesor
    return render(request, 'ingreso.html', {
        'tareas': tareas
    })


def Tareas_Ingreso(request):

    if request.method == 'GET': 
        return render(request, 'tareas_cliente.html', {
            'form': form_cliente
        })
    else:
        try:
            form = form_cliente(request.POST)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.usuario = request.user
            nueva_tarea.save()
            return redirect('ingreso')
        except ValueError:
            return render(request, 'tareas_cliente.html', {
            'form': form_cliente,
            'error':'Por Favor Chequea los Datos Ingresados'
        })

def Salir(request):
    logout(request)
    return redirect('home')


def Signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Nombre de Usuario o Contraseña Invalida'
            })

        else:
            login(request, usuario)
            return redirect('ingreso')

def notas(request, notas_id ):
    lista = get_object_or_404(Panel_Cliente, pk=notas_id)
    return render (request, 'notas.html', {
        'tareas':lista
    })


