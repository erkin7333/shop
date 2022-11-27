from django import template
from main.models import Category
register = template.Library()

@register.inclusion_tag('main/menu.html')
def menu():
    categories = Category.objects.all()
    return {'categories': categories}