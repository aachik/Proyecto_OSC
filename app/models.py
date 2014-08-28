from django.db import models

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

class TiposRedesSociales(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name_plural = "Tipos de redes sociales"
        verbose_name = "tipo de red social"

class RedSocial(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.ManyToManyField(TiposRedesSociales)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Redes sociales"
        verbose_name = "Red social"

class Organizacion(models.Model):
    nombre = models.CharField(max_length=150)
    poblacion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    fecha = models.DateField()
    telefono = models.CharField(max_length=15)
    dias = models.CharField(max_length=200)
    iniciohora = models.TimeField()
    finhora = models.TimeField()
    nombrecontacto = models.CharField(max_length=150)
    numeropersonas = models.CharField(max_length=3)
    recursos = models.CharField(max_length=255)
    tipo = models.ForeignKey(TipoOrganizacion)
    actividades = models.ManyToManyField(Actividades)
    areas = models.ManyToManyField(AreasInteres)
    red = models.ForeignKey(RedSocial)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "organizaciones"
        verbose_name = "organizacion"
