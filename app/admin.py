from django.contrib import admin

from app.models import Organizacion
from app.models import Actividades
from app.models import AreasInteres
from app.models import TipoOrganizacion
admin.site.register(Organizacion)
admin.site.register(AreasInteres)
admin.site.register(Actividades)
admin.site.register(TipoOrganizacion)