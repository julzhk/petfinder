from django import template

from petgallery.models import Animal

register = template.Library()


@register.inclusion_tag('animal_tile.html')
def animal_tile(animal: Animal):
    return {'animal': animal}
