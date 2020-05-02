from django import template

register = template.Library()


@register.filter(name='split')
def slpit_filter(value, arg):
    return value.split(arg)


@register.filter(name='get_date')
def get_date_filter(value, arg):

    if arg == 'day':
        return value.split('-')[2]
    elif arg == 'month':
        return value.split('-')[1]
    elif arg == 'day_n':
        return value.split('-')[3]
    else:
        return None
