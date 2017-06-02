"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite.views import current_datetime
from CRUD import views

urlpatterns = [
    #mysite
    url(r'^mysite/', current_datetime),
    url(r'^admin/', admin.site.urls),
    url(r'^sitios/', views.view_sitios),
    url(r'^sitios-edit/', views.sitios_edit),
    url(r'^edit_sitio/id=(\d{1,2})', views.sitios_edit),
    url(r'^empleados_sitio/id=(\d{1,2})', views.empleados_sitio),
    url(r'^crear_sitio_form/', views.create_site_form),
    url(r'^create_site/', views.create_site),
    url(r'^updated_site/', views.sitios_edited),
    url(r'^delete_sitio/id=(\d{1,2})', views.sitios_delete),
    url(r'^crear_empleado_form/id=(\d{1,2})', views.crear_empleado_sitio_form),
    url(r'^create_employee/', views.crear_empleado_sitio),
    url(r'^delete_empleado/id=(\d{1,2})/site_id=(\d{1,2})', views.eliminar_empleado)
]
