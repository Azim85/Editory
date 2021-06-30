from django import template

register = template.Library()

@register.filter()
def lancut(value):
    return value[4:]