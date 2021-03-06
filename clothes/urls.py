"""clothes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from solid_i18n.urls import solid_i18n_patterns
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = _('Clothes Catalog')
admin.site.site_title = _('Clothes Catalog')
admin.site.index_title = _('Clothes Catalog')

urlpatterns = [
    # url(r'^(?P<filename>(robots.txt)|(humans.txt))$', home_files, name='home-files'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += solid_i18n_patterns(
    url(r'^', include('catalog.urls', namespace="catalog")),
    url(r'^admin/', include(admin.site.urls)),
)
