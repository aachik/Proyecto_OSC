from django.contrib import admin

from app.models import Organizacion
from app.models import Actividades
from app.models import AreasInteres
from app.models import RedSocial
from app.models import TipoOrganizacion
from app.models import TiposRedesSociales
admin.site.register(Organizacion)
admin.site.register(AreasInteres)
admin.site.register(Actividades)
admin.site.register(RedSocial)
admin.site.register(TipoOrganizacion)
admin.site.register(TiposRedesSociales)