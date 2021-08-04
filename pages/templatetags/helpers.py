from django import template

register = template.Library()

@register.filter()
def lancut(value):
    return value[4:]



@register.filter()
def get_number(value):
    return int(value)