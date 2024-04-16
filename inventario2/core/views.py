from django.shortcuts import render


# Create your views here.
def login_usuario(request):
    return render(request,'login_usuario.html')

def home(request):
    return render(request,'index.html')

def accion(request):
    return render(request,'accion.html')

def carreras(request):
    return render(request,'carreras.html')

def deporte(request):
    return render(request,'deporte.html')

def lucha(request):
    return render(request,'lucha.html')

def terror(request):
    return render(request,'terror.html')

def contacto(request):
    return render(request,'contacto.html')
