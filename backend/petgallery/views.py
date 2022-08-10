from django.shortcuts import render

from petgallery.models import Animals


def home(request):
    return render(request,
                  template_name='gallery_home.html',
                  context={'animals': Animals()})
