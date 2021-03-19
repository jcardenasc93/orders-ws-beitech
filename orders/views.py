"""Orders views"""

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

# Models
from orders.models import Product, CustomerProduct, Customer, Order, OrderDetail
# Serializers
from orders.serializers import OrderDetailSerializer, OrderSerializer
# utils
from orders.utils.order_creator import OrderCreator


class OrderViewSet(viewsets.ViewSet):
    """
    Simple ViewSet for create and list orders
    """
    serializer = OrderSerializer
    INVALID_REQUEST_MSG = "Invalid request. Please check request body"

    def _error_response(self, msg=None):
        """ Method that returns BAD_REQUEST """
        if msg:
            return Response(data=msg, status=400)
        return Response(data=self.INVALID_REQUEST_MSG, status=400)

    def list(self, request):
        """ Defines list queryset to retrieve """
        orders = Order.objects.all()
        orders = self.serializer(orders, many=True)
        return Response(data=orders.data, status=200)


    def create(self, request):
        """ Overrides create method to handle
        logic business for Order objects creation
        """
        try:
            order_creator = OrderCreator(request.data)
        except KeyError:
            return self._error_response()

        if not order_creator.check_valid_customer_product():
            error_msg = "Customer cannot order these products"
            return self._error_response(msg=error_msg)

        try:
            if order_creator.quantity_products_is_valid():
                order_creator.calcs_total()
            else:
                error_msg = "User exceeds maximum number of products"
                return self._error_response(msg=error_msg)
        except Exception:
            return self._error_response()


        # All checks passed
        order_info = order_creator.retrieve_order_info()
        serialize_data = self.serializer(data=order_info)
        if serialize_data.is_valid():
            # Records order
            order = serialize_data.save()
            order_creator.add_order_details(order)
            return Response(data=serialize_data.data)
        else:
            return Response(data=serialize_data.errors, status=400)
