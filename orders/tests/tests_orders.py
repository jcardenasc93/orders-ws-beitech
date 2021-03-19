""" tests_orders.py contains the test cases for orders app """

from django.test import TestCase
from orders.models import Order, OrderDetail, Customer, Product, CustomerProduct
from django.urls import reverse
import json


class OrderTestCase(TestCase):
    """ class that defines different test cases """

    def _create_products(self):
        """ Creates different products for test """
        self.product_a = Product.objects.create(
            name='Prodcut A',
            product_description='Brief description',
            price=100.00)
        self.product_b = Product.objects.create(
            name='Prodcut B',
            product_description='Brief description',
            price=100.00)
        self.product_c = Product.objects.create(
            name='Prodcut C',
            product_description='Brief description',
            price=100.00)
        self.product_d = Product.objects.create(
            name='Prodcut D',
            product_description='Brief description',
            price=100.00)
        self.product_e = Product.objects.create(
            name='Prodcut E',
            product_description='Brief description',
            price=100.00)
        self.product_f = Product.objects.create(
            name='Prodcut F',
            product_description='Brief description',
            price=100.00)

    def _create_customers(self):
        """ Creates customers for testing """
        self.customer_jose = Customer.objects.create(name='Jose',
                                                     email='jose@example.com')
        self.customer_nikola = Customer.objects.create(
            name='Nikola', email='nikola@example.com')

    def _create_customer_product(self):
        """ Creates customer and products relations for testing """
        CustomerProduct.objects.create(product_id=self.product_a,
                                       customer_id=self.customer_jose)
        CustomerProduct.objects.create(product_id=self.product_b,
                                       customer_id=self.customer_jose)
        CustomerProduct.objects.create(product_id=self.product_a,
                                       customer_id=self.customer_nikola)
        CustomerProduct.objects.create(product_id=self.product_c,
                                       customer_id=self.customer_jose)

    def _create_orders(self):
        """ Creates orders for testing """
        self.order_jose = Order.objects.create(
            customer_id=self.customer_jose,
            delivery_address='Principal Avenue',
            total=200.00)
        self.order_nikola = Order.objects.create(
            customer_id=self.customer_nikola,
            delivery_address='Secondary Avenue',
            total=300.00)

    def _create_orders_details(self):
        """ Creates orders details for testing """
        OrderDetail.objects.create(order_id=self.order_jose,
                                   product_id=self.product_a,
                                   quantity=1)
        OrderDetail.objects.create(order_id=self.order_jose,
                                   product_id=self.product_b,
                                   quantity=1)
        OrderDetail.objects.create(order_id=self.order_nikola,
                                   product_id=self.product_a,
                                   quantity=3)

    def setUp(self):
        self._create_products()
        self._create_customers()
        self._create_customer_product()
        self._create_orders()
        self._create_orders_details()

    def test_list_orders(self):
        """ List orders unit test """
        response = self.client.get(reverse('orders'))
        self.assertEqual(200, response.status_code)
        response = json.loads(response.content)
        self.assertEqual(2, len(response))
        jose_order = response[0]
        self.assertEqual(2, len(jose_order.get('order_details')))

