from django import template

register = template.Library()


@register.filter(name='friendly_name')
def friendly_name(name):
    return name.replace('_', ' ')
