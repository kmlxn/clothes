from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.conf import settings

from .models import Clothing, Option


def make_choice_url(filt, current_filters={}):
    from django.utils.http import urlencode
    import copy
    filters = copy.copy(current_filters)
    filters.update(filt)

    return reverse("catalog:filter_clothes") + "?" + urlencode(filters)


def make_filters_list(current_filters={}):
    filters = list(Clothing.get_filter_params())
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


def handle_request_params(request):
    # request.GET contain a list of values for each parameter
    # but we need only one value for each parameter, so we form new dict
    params = {key: request.GET[key] for key in request.GET}
    filters = {k: v for k, v in params.items() if k != "page"}
    page_num = int(params.get("page", 1))
    return filters, page_num


def get_index_page(request):
    return render_with_dynamic_options(request, "catalog/index.html", {
        "clothes": Clothing.objects.all(),
        "filters_list": make_filters_list(),
    })


def filter_clothes(request):
    filters, page_num = handle_request_params(request)
    clothes = Clothing.filter(filters)
    paginator = Paginator(clothes, settings.ITEMS_PER_PAGE)

    return render_with_dynamic_options(request, "catalog/filter.html", {
        "clothes": paginator.page(page_num),
        "filters_list": make_filters_list(filters),
        "page_num": page_num,
        "pages_num": paginator.num_pages,
    })


def get_contact_page(request):
    return render_with_dynamic_options(request, "catalog/contact.html")


def get_about_us_page(request):
    return render_with_dynamic_options(request, "catalog/about_us.html")


def render_with_dynamic_options(request, template, context=None):
    new_context = Option.get_dynamic_options()
    if context is not None:
        new_context.update(context)

    return render(request, template, new_context)
