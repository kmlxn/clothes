from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.utils.translation import ugettext as _, activate, deactivate
from django.conf import settings
import datetime

from .models import Clothing, Option, Order
from .forms import OrderForm

def make_filters_list(current_filters=None):
    if current_filters is None:
        current_filters = {}

    filters = list(Clothing.get_filter_params())
    filters_list = [
        {
            "caption": f.caption,
            "url_name": f.url_name,
            "choices": make_choices(f, current_filters.get(f.url_name, None)),
        } for f in filters
    ]

    return filters_list


def make_choices(filt, currently_chosen):
    return [
        {
            "caption": x.caption,
            "url_name": x.url_name,
            "is_currently_chosen": x.url_name == currently_chosen
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
    clothes = Clothing.objects.all()
    paginator = Paginator(clothes, settings.ITEMS_PER_PAGE)

    return render_with_dynamic_options(request, "catalog/index.html", {
        "clothes": paginator.page(1),
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


def handle_order(request):
    if request.method == 'POST':
        return handle_order_post(request)
    else:
        return render_order_page(request)


def render_order_page(request):
    form = OrderForm()
    order_status = 'success' if 'order_success' in request.COOKIES else None

    response = render_with_dynamic_options(request, "catalog/order.html", {
        'order_status': order_status,
        'form': form,
    })
    response.delete_cookie('order_success')

    return response


def handle_order_post(request):
    form = OrderForm(request.POST)

    if form.is_valid():
        response = handle_new_order(request)
    else:
        response = render_with_dynamic_options(request, "catalog/order.html", {
            'order_status': 'fail',
            'form': form,
        })

    return response


def handle_new_order(request):
    order = Order.objects.create(client_email = request.POST['client_email'],
        client_name = request.POST['client_name'],
        client_phone = request.POST['client_phone'],
        client_company = request.POST['client_company'],
        order_text = request.POST['order_text'])

    response = redirect(reverse('catalog:order'))
    response.set_cookie('order_success', '', max_age=1000)

    notificate_manager(order)

    return response


def notificate_manager(order):
    dynamic_options = Option.get_dynamic_options()

    activate(settings.LANGUAGE_CODE)

    subject = '{} - {} - {} {}'.format(dynamic_options['brand_name'],
        _('New order'), order.client_name, order.client_company)
    message = '{}\n{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: \n{}\n'.format(
        _('New order'),
        Order.get_verbose_name('client_name'), order.client_name,
        Order.get_verbose_name('client_company'), order.client_company,
        Order.get_verbose_name('client_email'), order.client_email,
        Order.get_verbose_name('client_phone'), order.client_phone,
        Order.get_verbose_name('order_text'), order.order_text)

    send_mail(subject, message, settings.EMAIL_HOST_USER,
        [dynamic_options['email']], fail_silently=False)

    deactivate()


def render_with_dynamic_options(request, template, context=None):
    new_context = Option.get_dynamic_options()
    if context is not None:
        new_context.update(context)

    return render(request, template, new_context)
