"""petfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from petAPI.views import grid_api, petapi
from petgallery.views import gallery, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pet_types_api', petapi, name='types_api'),
    path('grid_api', grid_api, name='grid_api'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('gallery', gallery, name='gallery'),
    path('', home, name='home'),
]
