from django import template

register = template.Library()

from datetime import datetime, timedelta


@register.simple_tag
def sizify(value):
    date_now = datetime.today() + timedelta(days=value)
    format_date = date_now.strftime("%d-%m-%Y")
    return str(format_date)


register.filter('sizify', sizify)


@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)


@register.simple_tag
def three_time(value):
    date_now = datetime.today() + timedelta(days=value)
    format_date = date_now.strftime("%d-%m-%Y")
    return str(format_date)


register.filter('three_time', three_time)
