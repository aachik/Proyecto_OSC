from django.shortcuts import render_to_response
from django.core.paginator import  EmptyPage, Paginator, InvalidPage
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.context_processors import csrf

from app.models import *

def organizacion(request, pk):
    idorganizacion = Organizacion.objects.get(pk = int(pk))


    return render_to_response("organizacion.html", dict(organizacion = idorganizacion, usuario = request.user))

def main(request):
    organizacion = Organizacion.objects.all().order_by("-fecha")
    paginator = Paginator(organizacion,10)

    try:
        pagina=int(request.GET.get("page",'1'))
    except ValueError: pagi
    na = 1

    try:
        organizacion = paginator.page(pagina)
    except(InvalidPage,EmptyPage):
        organizacion = paginator.page(paginator.num_pages)

    return render_to_response("inicio.html", dict(organizacion = organizacion, usuario = request.user))

def form(request):
    organizacion = Organizacion.objects.all().order_by("-fecha")


    return render_to_response("form.html", dict(organizacion = organizacion, usuario = request.user))

def admin(request):

    return render_to_response("/admin/")