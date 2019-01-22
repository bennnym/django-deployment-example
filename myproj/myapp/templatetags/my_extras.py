from django import template

register = template.Library()

@register.filter(name='cutter')
def  cutter(value, arg):
    """
    This is me creating a custom template filter
    This cuts out all values of arg from the string!
    """
    return value.replace(arg,'')

# this registers the custom filters - this is a way to do it besides decorators!
# first argument is what you call the filter and the second is just the name of the function above
#register.filter('cutter', cutter)
