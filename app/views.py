from django.shortcuts import render_to_response, redirect,RequestContext
from django.core.paginator import  EmptyPage, Paginator, InvalidPage
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.context_processors import csrf
from django.template import Context

from .forms import *

from app.models import *

def organizacion(request, pk):
    idorganizacion = Organizacion.objects.get(pk = int(pk))


    return render_to_response("organizacion.html", dict(organizacion = idorganizacion, usuario = request.user))

def main(request):
    organizacion = Organizacion.objects.all().order_by("-fechaInicio")
    paginator = Paginator(organizacion,10)
    # form = BuscarInteresForm(request.GET or None)
    # if form.is_valid():
    #     save_it=form.save(commit=False)
    #     save_it.save()
    #     return redirect("/")

    try:
        pagina=int(request.GET.get("page",'1'))
    except ValueError:
        pagina = 1

    try:
        organizacion = paginator.page(pagina)
    except(InvalidPage,EmptyPage):
        organizacion = paginator.page(paginator.num_pages)

    return render_to_response("inicio.html",locals(),context_instance=RequestContext(request))

def formulario(request):
    form = OrganizacionForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        return redirect('/')
    return render_to_response("form.html",  locals(),context_instance=RequestContext(request))

def search(request):
    query = request.GET['q']
    try:
        org=Organizacion.objects.get(nombre__startswith=query )

    except Organizacion.DoesNotExist:
        org='None'


    return render_to_response('resultados.html',dict(organizacion = org))



def admin(request):

    return render_to_response("/admin/")


def contacto(request):

    return render_to_response("contacto.html")