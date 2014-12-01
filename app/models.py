from django.db import models
import datetime
# Create your models here.


class TipoOrganizacion(models.Model):
    nombre = models.CharField(max_length=140)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Organizacion"


class Actividades(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Actividades"


class AreasInteres(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Areas de interes"
        verbose_name = "Area de interes"


class Organizacion(models.Model):
    nombre = models.CharField(max_length=150)
    poblacion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    fechaInicio = models.DateField()
    telefono = models.CharField(max_length=10)
    dias = models.CharField(max_length=200)
    horario = models.CharField(max_length=30)
    nombrecontacto = models.CharField(max_length=150)
    numeropersonas = models.CharField(max_length=4)
    recursos = models.CharField(max_length=255)
    tipo = models.ForeignKey(TipoOrganizacion)
    actividades = models.ManyToManyField(Actividades)
    areas = models.ManyToManyField(AreasInteres)
    facebook = models.CharField(max_length=150)
    twitter = models.CharField(max_length=140)
    correo = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "organizaciones"
        verbose_name = "organizacion"
