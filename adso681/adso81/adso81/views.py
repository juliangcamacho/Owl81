from django.shortcuts import render

def index(request):
    return render(request,'index.html',{
        #context
    })

def inventarios(request):
    return render(request,'inventarios.html',{
        #context
    })
def ic(request):
    return render(request,'ic.html',{
        #context
    })    
def blog(request):
    return render(request,'blog.html',{
        #context
    })
def donaciones(request):
    return render(request,'donaciones.html',{
        #context
    })
def login(request):
    return render(request,'login_owl_system.html',{
        #context
    })
def novedades(request):
    return render(request,'novedades.html',{
        #context
    })
def regis_donacion(request):
    return render(request,'regis_donacion.html',{
        #context
    })
def regis_novedad(request):
    return render(request,'registrar_novedades.html',{
        #context
    })
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html', {
        
    })

