from django.shortcuts import render
from django.http import HttpResponse
from CRUD.models import Sitio, Empleado
from django.shortcuts import render_to_response

# Create your views here.
def view_sitios(request):
    #return render(request, 'crud_site_list.html')
    #e = Empleado(nombre='jorge', apellidos='cano', telefono='99909999', correo='jorge@walook')
    #s = Sitio(nombre='hola', direccion='psh')
    #e.save()
    #s.save()
    #s.empleados.add(e)

    sitios_list = Sitio.objects.all()
    return render_to_response('crud_site_list.html', {'sitio_list' : sitios_list})

def empleados_sitio(request):
    sitio = Sitio.objects.get(id=1)
    e = Empleado(nombre='jorge', apellidos='cano', telefono='99909999', correo='jorge@walook')
    e.save()
    sitio.empleados.add(e)
    sitio.save()
    empleados = sitio.empleados.filter(nombre='jorge')
    #sitio.objects.
    return render_to_response('crud_employee_in_site_list.html', {'empleados':sitio.empleados.all()})

def sitios_edit(request):
    if 'NOMBRE CAMPO' in request.GET:
        message = 'hola g g g'
    else:
        message = 'uwu'
    return HttpResponse(message)

def sitios_edit_final(request):
    if 'site_name' in request.GET:
        site_name = request.GET['site_name']

        s = request.GET
        new_sitio = s.save()
        message = 'hola g g g'
    else:
        message = 'uwu'
    return HttpResponse(message)

