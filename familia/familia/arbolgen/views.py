from django.shortcuts import render
from arbolgen.models import Familias

#Creando funcion para crear a las familias en la base de datos
#Se crearon 3 familias con sus respectivos datos

def create_family(request):
    #familia 1
    #new_family = Familias.objects.create(name_family = 'Gomez', num_members = 4, favorite_day_week = 'Miercoles')
    
    #familia 2
    #new_family = Familias.objects.create(name_family = 'Fernandez', num_members = 3, favorite_day_week = 'Sabado')
    
    #familia 3
    new_family = Familias.objects.create(name_family = 'Suarez', num_members = 5, favorite_day_week = 'Domingo')
    context = {
        'new_family':new_family
    }
    return render(request, 'arbol-familias.html', context = context)

#Creando funcion para ver el listado de las familias en el template
def list_family(request):
    families = Familias.objects.all()
    context = {
        'families':families,
    }
    return render(request, 'list-family.html', context= context) #este sera el url que utilizaremos para ver el trabajo