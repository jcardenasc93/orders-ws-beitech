""" Orders urls.py """

from django.urls import path
from orders.views import OrderViewSet

urlpatterns = [
    path(r'orders/',
         OrderViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }),
         name='orders')
]
