from django import template

register = template.Library()

@register.filter
def addstr(arg):
    """concatenate arg1 & arg2"""
    return set(arg)