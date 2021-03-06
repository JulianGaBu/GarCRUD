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
    return render_to_response('crud_employee_in_site_list.html', {'sitio': sitio})

def crear_empleado_sitio_form(request, id_sitio):
    sitio = Sitio.objects.get(id=id_sitio)
    return render_to_response('crud_create_employee.html',{'sitio':sitio})

def crear_empleado_sitio(request):
    sitio = Sitio.objects.get(id=request.GET['sitio_id'])
    ename = request.GET['employee_name']
    elast = request.GET['employee_last_name']
    email = request.GET['employee_email']
    enum = request.GET['employee_phoenumber']
    employee = Empleado(nombre=ename,apellidos=elast,telefono=enum, correo=email)
    employee.save()
    sitio.empleados.add(employee)
    sitio.save()
    return render_to_response('redirect_employees.html', {'site': sitio})


def sitios_edit(request, id):
    sitio = Sitio.objects.get(id=id)
    return render_to_response('crud_update_site.html', {'sitio': sitio})

def sitios_delete(request, id):
    sitio = Sitio.objects.get(id=id)
    sitio.delete()
    #todo change response
    return render_to_response('redirect_sites.html')

def sitios_edited(request):
    sitio = Sitio.objects.get(id=request.GET['site_id'])
    sitio.nombre = request.GET['site_name']
    sitio.direccion = request.GET['site_dir']
    sitio.save()
    #todo change response
    return render_to_response('redirect_sites.html')


def create_site(request):
    if 'site_name' in request.GET:
        site_name = request.GET['site_name']
        site_dir = request.GET['site_dir']
        site = Sitio(nombre=site_name, direccion=site_dir)
        site.save()
    #todo js response
    return render_to_response('redirect_sites.html')

def eliminar_empleado(request, em_id, site_id):
    empleado = Empleado.objects.get(id=em_id)
    empleado.delete()
    return render_to_response('redirect_employees.html', {'site': Sitio.objects.get(id=site_id)})

def editar_empleado(request, em_id):
    empleado = Empleado.objects.get(id=em_id)
    return render_to_response('crud_update_employee.html', {'empleado':empleado})
