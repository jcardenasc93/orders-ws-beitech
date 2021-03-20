"""Orders views"""

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse
import requests
import datetime
from dateutil.relativedelta import relativedelta
import json

# Models
from orders.models import Product, CustomerProduct, Customer, Order, OrderDetail
# Serializers
from orders.serializers import OrderDetailSerializer, OrderSerializer
# utils
from orders.utils.order_creator import OrderCreator
from orders.utils.params_validator import validate_query_params


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

    def list(self, request, customer_id=None):
        """ Defines list queryset to retrieve """
        data = validate_query_params(request.GET, customer_id)
        if data is None:
            error_msg = "Invalid request. Please check filter criteria"
            return self._error_response(error_msg)

        orders = Order.objects.filter(customer_id=data.get('customer'),
                                      creation_date__gte=data.get('start_date'),
                                      creation_date__lte=data.get('end_date'))
        orders = self.serializer(orders, many=True)
        return Response(data=orders.data, status=200)

    def create(self, request, customer_id=None):
        """ Overrides create method to handle
        logic business for Order objects creation
        """
        try:
            order_creator = OrderCreator(request.data, customer_id)
        except KeyError:
            return self._error_response()
        except Customer.DoesNotExist:
            error_msg = "User not found"
            return self._error_response(error_msg)

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


@api_view(['GET', 'POST'])
def render_view(request):
    """ This view render the HTML template based on
    the HTTP method
    """
    ORDERS_TEMPLATE = 'orders/client_orders.html'
    customers = Customer.objects.all()

    if request.method == 'GET':
        context = {"customers": customers}
        return render(request, ORDERS_TEMPLATE, context)

    if request.method == "POST":
        # Calcs month ago date
        today = datetime.date.today()
        month_ago = today - relativedelta(months=1)
        dates = {'start_date': month_ago, 'end_date': today}
        customer_id = request.POST.get('customer_id')
        # Builds the url to send the request
        host = request.get_host()
        protocol = 'https://' if request.is_secure() else 'http://'
        url = f"{protocol}{host}/orders/customer/{customer_id}?start_date={dates.get('start_date')}&end_date={dates.get('end_date')}"
        response = requests.get(url)
        response = json.loads(response.content)
        # Builds context to pass it to template
        context = {"customers": customers, "orders": response}
        return render(request, ORDERS_TEMPLATE, context)

