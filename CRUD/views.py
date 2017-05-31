from django.shortcuts import render
from django.http import HttpResponse
from CRUD.models import Sitio, Empleado
from django.shortcuts import render_to_response


# Create your views here.
def view_sitios(request):
    sitios_list = Sitio.objects.all()
    return render_to_response('crud_site_list.html', {'sitio_list': sitios_list})

def create_site_form(request):
    return render_to_response('crud_create_site.html')

def empleados_sitio(request, id):
    sitio = Sitio.objects.get(id=id)
    return render_to_response('crud_employee_in_site_list.html', {'empleados': sitio.empleados.all()})

def sitios_edit(request, id):
    sitio = Sitio.objects.get(id=id)
    return render_to_response('crud_update_site.html', {'sitio':sitio})

def sitios_edited(request):
    if 'id' in request.GET:
        sitio = Sitio.objects.get(id=request.GET['id'])



def create_site(request):
    if 'site_name' in request.GET:
        site_name = request.GET['site_name']
        site_dir = request.GET['site_dir']
        site = Sitio(nombre=site_name, direccion=site_dir)
        site.save()
        message = 'saved'
    else:
        message = 'uwu'
    return render_to_response('crud_site_list.html')
