""" tests_orders.py contains the test cases for orders app """

from django.test import TestCase
from orders.models import Order, OrderDetail, Customer, Product, CustomerProduct
from django.urls import reverse
import json
import decimal
import datetime


class OrderTestCase(TestCase):
    """ class that defines different test cases """

    def _create_products(self):
        """ Creates different products for test """
        default_price = decimal.Decimal('100.99')
        self.product_a = Product.objects.create(
            name='Prodcut A',
            product_description='Brief description',
            price=default_price)
        self.product_b = Product.objects.create(
            name='Prodcut B',
            product_description='Brief description',
            price=default_price)
        self.product_c = Product.objects.create(
            name='Prodcut C',
            product_description='Brief description',
            price=default_price)
        self.product_d = Product.objects.create(
            name='Prodcut D',
            product_description='Brief description',
            price=default_price)
        self.product_e = Product.objects.create(
            name='Prodcut E',
            product_description='Brief description',
            price=default_price)
        self.product_f = Product.objects.create(
            name='Prodcut F',
            product_description='Brief description',
            price=default_price)

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
        # Success case
        from django.test import Client
        client = Client()
        today = datetime.date.today()
        dates = {'start_date': str(today), 'end_date': str(today)}
        response = client.get(reverse('orders', args=[self.customer_jose.pk]),
                              dates)
        self.assertEqual(200, response.status_code)
        response = json.loads(response.content)
        self.assertEqual(1, len(response))

        # Empty response
        yesterday = today - datetime.timedelta(days=1)
        dates = {'start_date': str(yesterday), 'end_date': str(yesterday)}
        response = client.get(reverse('orders', args=[self.customer_jose.pk]),
                              dates)
        self.assertEqual(200, response.status_code)
        response = json.loads(response.content)
        self.assertEqual(0, len(response))

    def test_fail_list_orders(self):
        """ Tests fail cases for list orders """
        # No dates given
        dates = {'start_date': 'any-input', 'end_date': 'any_input'}
        from django.test import Client
        client = Client()
        response = client.get(reverse('orders', args=[self.customer_jose.pk]))
        self.assertEqual(400, response.status_code)

        # Bad dates given
        response = client.get(reverse('orders', args=[self.customer_jose.pk]),
                              dates)
        self.assertEqual(400, response.status_code)

        # User not found
        response = client.get(reverse('orders', args=[5]), dates)
        self.assertEqual(400, response.status_code)

    def test_create_order(self):
        """ Create orders test cases """
        # Success case
        payload = {
            "delivery_address": "Django street 3.1",
            "products": [{
                "product_id": self.product_a.pk,
                "quantity": 2
            }]
        }
        response = self.client.post(reverse('orders',
                                            args=[self.customer_jose.pk]),
                                    json.dumps(payload),
                                    content_type='application/json')
        self.assertEqual(200, response.status_code)
        # Check total order
        total = json.loads(response.content).get('total')
        expected_total = payload.get('products')[0].get(
            'quantity') * self.product_a.price
        self.assertEqual(str(expected_total), total)

    def test_fail_create_order(self):
        """ Fail create order test cases """
        # Fail case: Missing parameters
        payload = {
            "customer_id": self.customer_jose.pk,
            "delivery_address": "Django street 3.1",
        }
        response = self.client.post(reverse('orders',
                                            args=[self.customer_jose.pk]),
                                    json.dumps(payload),
                                    content_type='application/json')
        self.assertEqual(400, response.status_code)

        # Fails case: Invalid user products
        payload['products'] = [{
            "product_id": self.product_d.pk,
            "quantity": 1
        }, {
            "product_id": self.product_a.pk,
            "quantity": 1
        }]
        response = self.client.post(reverse('orders',
                                            args=[self.customer_jose.pk]),
                                    json.dumps(payload),
                                    content_type='application/json')
        self.assertEqual(400, response.status_code)

        # User not found
        response = self.client.post(reverse('orders', args=[5]),
                                    json.dumps(payload),
                                    content_type='application/json')
        self.assertEqual(400, response.status_code)
