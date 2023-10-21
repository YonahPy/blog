from django import template
from django.utils.timesince import timesince
from django.utils.timezone import now

register = template.Library()

@register.filter
def custom_timesince(value):
    return timesince(value, now())