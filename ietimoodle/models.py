from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Centro(models.Model):
    nombre = models.CharField(max_length=200)
    localitat = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=255)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
class Ejercicio(models.Model):
    nombre = models.CharField(max_length=200)
    ponderacion = models.IntegerField(default=0)
    visibilidad = models.BooleanField(default=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class NivelPrivacidad(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE) 
    privacidad = models.ForeignKey(NivelPrivacidad, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_username()

class Entrega(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    estado = models.BooleanField()
    cualificacion = models.IntegerField(default=0)
    archivo = models.FileField(upload_to="./entregas/")
    fecha_entrega = models.DateTimeField()
    comentario_profesor = models.CharField(max_length=255)
    comentario_alumno = models.CharField(max_length=255)
    def __str__(self):
        return self.ejercicio.nombre

class Suscripcion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=200)
    def __str__(self):
        return self.tipo
