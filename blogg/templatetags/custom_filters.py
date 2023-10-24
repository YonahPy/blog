from django import template
from django.utils.timesince import timesince
from django.utils.timezone import now, make_aware, utc
from datetime import datetime

register = template.Library()

@register.filter
def format_date(value):
    if value and len(value) >=10:
        return value[:10]
    return value