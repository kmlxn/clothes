from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_index_page, name='index_page'),
    url(r'^filter$', views.filter_clothes, name='filter_clothes'),
    url(r'^contact', views.get_contact_page, name='contact'),
    url(r'^about_us', views.get_about_us_page, name='about_us'),
    url(r'^order', views.handle_order, name='order'),
]
