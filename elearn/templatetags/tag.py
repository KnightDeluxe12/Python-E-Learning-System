from django import template

register = template.Library()


@register.simple_tag

def converttostring(name):
    name1 = str(name)

    return name1