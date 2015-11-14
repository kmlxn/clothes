from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.getIndexPage, name='index_page'),
]
