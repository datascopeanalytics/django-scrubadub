import re

from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def word_wrapper(s):
    """place span tags around all words"""
    result = ''
    last_char = 0
    in_span = False
    for match in re.finditer(r'\b', s):

        # gets the whitespace
        result += s[last_char:match.start()]

        # adds span tags
        if in_span:
            result += '</span>'
        else:
            result += '<span data-beg="%d">' % match.start()

        # adds match
        result += s[match.start():match.end()]

        # updates things for next time
        last_char = match.end()
        in_span = not in_span

    # don't forget to add the rest
    result += s[last_char:]
    return mark_safe(result)
