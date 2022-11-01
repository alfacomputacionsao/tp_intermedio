import email
from mailbox import NoSuchMailboxError
from re import M
from this import d
from tkinter import Y
from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class Panel_Cliente (models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    dni = models.IntegerField()
    email = models.EmailField()
    creado=models.DateTimeField(auto_now_add=True)
    modificado=models.DateTimeField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "ID de Alumno N°", self.id, "Nombre de Alumno", self.nombre, "Creado Por: ", self.usuario



