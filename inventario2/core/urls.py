from django.urls import path
from .views import login_usuario, home, accion, carreras, deporte, lucha, terror, contacto

urlpatterns = [
    path('', login_usuario, name="login_usuario"),
    path('home', home, name="home"),
    path('accion', accion, name="accion"),
    path('carreras', carreras, name="carreras"),
    path('deporte', deporte, name="deporte"),
    path('lucha', lucha, name="lucha"),
    path('terror', terror, name="terror"),
    path('contacto', contacto, name="contacto"),
]
