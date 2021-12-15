from django import template
from datetime import date

today = date.today()
register = template.Library()

@register.filter
def borrowed_days(borrowed, returned=today):
    return (returned - borrowed).days