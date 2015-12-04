from django import template

register = template.Library()

@register.inclusion_tag('catalog/filters_partial.html')
def render_filters(filters_list):
    return {'filters_list': filters_list}

@register.inclusion_tag('catalog/clothes_partial.html')
def render_clothes_grid(clothes):
    return {'clothes': clothes}