from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_index_page, name='index_page'),
    url(r'^filter$', views.filter_clothes, name='filter_clothes'
    ),
]
