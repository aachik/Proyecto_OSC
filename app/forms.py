__author__ = 'abdul'

from django import forms
from .models import *


class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = Organizacion


        exclude = ['']


class BuscarInteresForm(forms.ModelForm):
    class Meta:
        model = Organizacion

        exclude=['nombre','poblacion','direccion','fechaInicio','telefono','dias','horario','nombrecontacto','numeropersonas',
                 'recursos','tipo','actividades','facebook','twitter','correo']
