""" Orders urls.py """

from django.urls import path
from orders.views import OrderViewSet, render_view

urlpatterns = [
        path(r'', render_view, name='index'),
        path(r'orders/customer/<int:customer_id>',
         OrderViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }),
         name='orders')
]
