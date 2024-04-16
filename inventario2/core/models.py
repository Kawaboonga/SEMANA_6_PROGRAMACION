from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Usuario(models.Model):
    run = models.IntegerField(primary_key=True, verbose_name='run')
    username = models.CharField(max_length=10, min_length=6, verbose_name='username')
    nombres = models.CharField(max_length=120, min_length=8,  verbose_name='nombres')
    apellidos = models.CharField(max_length=60, min_length=8, verbose_name='apellidos')
    password = models.CharField(max_length=128, min_length=8, verbose_name='password')
    perfil = models.IntegerField(null=True, blank=True, verbose_name='perfil')

def validar_caracteres_especiales(value):
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
    for caracter in value:
        if caracter in caracteres_especiales:
            return
    raise ValidationError('El campo debe contener al menos un carácter especial.')