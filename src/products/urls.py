from django.conf.urls import url

from .views import (
    ProductListView,
    ProductDetailView,
)

app_name = 'product'
urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list_view'),
    url(r'^detail/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='detail_view'),

]
