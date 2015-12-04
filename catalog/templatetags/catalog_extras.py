from django import template

register = template.Library()

@register.inclusion_tag('catalog/filters_partial.html')
def render_filters(filters_list):
    return {'filters_list': filters_list}