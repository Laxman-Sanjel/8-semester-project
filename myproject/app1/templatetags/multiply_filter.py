from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0.0  # Handle the case where either value or arg cannot be converted to float

register.filter('multiply', multiply)


@register.filter(name='minus')
def divideby(value, arg):
    try:
        return value - arg
    except ZeroDivisionError:
        return 0  # Handle division by zero gracefully