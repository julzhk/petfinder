from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from petgallery.models import Animal, AnimalTypes, RateLimitError


@csrf_exempt
def home(request):
    try:
        return render(request,
                      template_name='gallery_home.html',
                      context={'animals': AnimalTypes()})
    except RateLimitError:
        return HttpResponse('Petfinder API rate limit exceeded. Please wait.')


@csrf_exempt
def gallery(request):
    animal_type = request.GET.get('type')
    page = int(request.GET.get('page', 1))
    try:
        animals = Animal.populate(animal_type=animal_type, page=page)
        return render(request,
                      template_name='gallery.html',
                      context={
                          'animals': animals,
                          'animal_type': animal_type,
                          'next_page': page + 1
                      })
    except RateLimitError:
        return HttpResponse('Petfinder API rate limit exceeded. Please wait.')
