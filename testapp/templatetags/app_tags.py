from django import template
import datetime

register=template.Library()

@register.simple_tag(name="get_date")
def get_date():
    now =datetime.datetime.now()
    return now
@register.filter
def quotes(data):
    s='""'+str(data)+'""'
    return s
