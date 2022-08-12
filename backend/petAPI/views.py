from django.conf import settings
from django.http import JsonResponse

from petgallery.models import Animal, AnimalType, AnimalTypes


def petapi(request):
    if settings.FAKE_API:
        types = generate_fake_animal_types()
    else:
        types = AnimalTypes()
    return JsonResponse(types, safe=False, headers={'Access-Control-Allow-Origin': '*'})


def grid_api(request):
    page = 1
    animal_type = request.GET.get('animal')
    if settings.FAKE_API:
        animals = generate_fake_grid()
    else:
        animals = Animal.populate(animal_type=animal_type, page=page)
    return JsonResponse(animals, safe=False, headers={'Access-Control-Allow-Origin': '*'})


def generate_fake_animal_types():
    data = [AnimalType(name='lion'),
            AnimalType(name='jackal'),
            AnimalType(name='bobcat')]
    types = [d.to_dict() for d in data]
    return types


def generate_fake_grid():
    data = [Animal(name='dog A'),
            Animal(name='dog B'),
            Animal(name='dog C')]
    return [d.to_dict() for d in data]
