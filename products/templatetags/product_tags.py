from django import template

register = template.Library()


@register.filter(name='friendly_name')
def friendly_name(name):
    """
    Converts a string with underscores into a human-readable format
    by replacing underscores with spaces.

    **Arguments:**
    - `name`: A string to be formatted.

    **Returns:**
    - A string where all underscores are replaced with spaces.
    """
    return name.replace('_', ' ')
