"""Orders views"""

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

# Models
from orders.models import Product, CustomerProduct, Customer, Order, OrderDetail
# Serializers
from orders.serializers import OrderDetailSerializer, OrderSerializer


class OrderViewSet(viewsets.ViewSet):
    """
    Simple ViewSet for create and list orders
    """
    serializer = OrderSerializer

    def list(self, request):
        """ Defines list queryset to retrieve """
        orders = Order.objects.all()
        orders = self.serializer(orders, many=True)
        return Response(data=orders.data, status=200)

    def create(self, request):
        """ Overrides create method to handle
        logic business for Order objects creation
        """
        serialize_data = self.serializer(data=request.data)
        self.perform_create(serialize_data)
