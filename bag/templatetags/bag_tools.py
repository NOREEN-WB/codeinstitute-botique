""" imports """
from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ to calculate total amount on upodate """
    return price * quantity
