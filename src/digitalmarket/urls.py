"""digitalmarket URL Configuration

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

from products.views import (
        detail_view,
        list_view,
        detail_slug_view,
        create_view,
        update_view
        )

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', list_view, name='list_view'),
    url(r'^create/$', create_view, name='create_view'),
    url(r'^detail/(?P<object_id>\d+)/$', detail_view, name='detail_view'),
    url(r'^detail/(?P<object_id>\d+)/update/$', update_view, name='update_view'),
    url(r'^detail/(?P<slug>[\w-]+)/$', detail_slug_view, name='detail_slug_view'),
    url(r'^products/', include('products.urls', namespace='products')),
]
