
from django.contrib import admin
from django.urls import path

from arbolgen.views import create_family, list_family

urlpatterns = [
    path('admin/', admin.site.urls),
    path('arbol-familias/', create_family, name='arbol-familia'),
    path('list-family/', list_family, name='lista-families') #Pagina que se utilizara para ver el resultado del ejercicio
    
]
