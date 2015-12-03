from django.shortcuts import render
from django.core.urlresolvers import reverse

from .models import Clothing


def make_choice_url(filt, current_filters={}):
    from django.utils.http import urlencode
    import copy

    filters = copy.copy(current_filters)
    filters.update(filt)

    return reverse("catalog:filter_clothes") + "?" + urlencode(filters)


def make_filters_list(current_filters={}):
    filters = list(Clothing.filters)
    filters_list = [
        {
            "caption": f.caption,
            "url_name": f.url_name,
            "choices": make_choices(f, current_filters),
        } for f in filters
    ]

    return filters_list


def make_choices(filt, current_filters):
    return [
        {
            "caption": x.caption,
            "url_name": x.url_name,
            "real_url": make_choice_url(
                {filt.url_name: x.url_name},
                current_filters
            )
        } for x in filt.choices
    ]


def get_request_params(request):
    # request.GET contain a list of values for each parameter
    # but we need only one value for each parameter, so we form new dict
    params = {prm: request.GET[prm] for prm in request.GET}
    return params


def get_index_page(request):
    return render(request, "catalog/index.html", {
        "clothes": Clothing.objects.all(),
        "filters_list": make_filters_list(),
    })


def filter_clothes(request):
    filtering_params = get_request_params(request)

    return render(request, "catalog/filter.html", {
        "clothes": Clothing.filter(filtering_params),
        "filters_list": make_filters_list(filtering_params),
    })
