from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from petgallery.models import Animal, AnimalTypes


@csrf_exempt
def home(request):
    return render(request,
                  template_name='gallery_home.html',
                  context={'animals': AnimalTypes()})


@csrf_exempt
def gallery(request):
    animal_type = request.GET.get('type')
    page = int(request.GET.get('page', 1))
    animals = Animal.populate(animal_type=animal_type, page=page)
    return render(request,
                  template_name='gallery.html',
                  context={
                      'animals': animals,
                      'animal_type': animal_type,
                      'next_page': page + 1
                  })
