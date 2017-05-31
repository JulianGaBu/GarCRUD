from django.shortcuts import render
from django.http import HttpResponse
from CRUD.models import Sitio, Empleado
from django.shortcuts import render_to_response

# Create your views here.
def view_sitios(request):
    #return render(request, 'crud_site_list.html')
    #s = Sitio(nombre='hola', direccion='psh')
    #s.save()
    sitios_list = Sitio.objects.all()
    return render_to_response('crud_site_list.html', {'site_list' : sitios_list})

def sitios_edit(request):
    if 'NOMBRE CAMPO' in request.GET:
        message = 'hola g g g'
    else:
        message = 'uwu'
    return HttpResponse(message)

def sitios_edit_final(request):
    if 'NOMBRE CAMPO AGREGAR' in request.GET:

        s = request.GET
        new_sitio = s.save()
        message = 'hola g g g'
    else:
        message = 'uwu'
    return HttpResponse(message)

