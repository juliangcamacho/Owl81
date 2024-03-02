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