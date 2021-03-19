""" Request validator module """

from orders.models import Product, Customer, CustomerProduct, OrderDetail
import decimal
from functools import reduce


class OrderCreator:
    """ This class allows perform required logic
    for incoming orders
    """

    def __init__(self, request_data: dict):
        self.customer = Customer.objects.get(pk=request_data['customer_id'])
        self.delivery_address = request_data['delivery_address']
        self.products_in_request = request_data['products']
        self.products_ids = [
            product['product_id'] for product in self.products_in_request
        ]
        self.total = decimal.Decimal(0.00)
        self.products = self._retrieve_products()

    def _retrieve_products(self):
        """ This method retrieve the specified products
        Args:
            products_ids (list): A list object with the unique products identifiers
        Returns:
            products (QuerySet): The queryset to be excecuted to retrieve products info
        """
        products = Product.objects.filter(pk__in=self.products_ids).values(
            'product_id', 'price')
        return products

    def quantity_products_is_valid(self):
        """ Validate the business constraint that allow max
        products by order
        Returns:
            (bool): True if total quantity doesn't exceeds the maximum
                    products allowed
        """
        MAX_PRODUCTS = 5
        quantities = [
            product['quantity'] for product in self.products_in_request
        ]
        total = reduce(lambda x, y: x + y, quantities)
        return total <= MAX_PRODUCTS

    def calcs_total(self):
        """ Return the total price for the order based
        on the products included in the order
        Args:
            products (list): Result of the Product query
            products_quantity (list): The products list related to the order
        """
        total = decimal.Decimal(0.00)
        for related_product in self.products_in_request:
            for product in self.products:
                if product.get('product_id') == related_product.get(
                        'product_id'):
                    total += product.get('price') * related_product.get(
                        'quantity')
        self.total = total

    def check_valid_customer_product(self):
        """This method checks if the customer could order the
        specified products.
        Returns:
            (bool): True if all the products are valid for the customer
        """
        # Check for CustomerProducts objects
        valid_products = list(
            CustomerProduct.objects.filter(customer_id=self.customer,
                                           product_id__in=self.products_ids))

        return len(valid_products) == len(self.products_in_request)

    def retrieve_order_info(self):
        """This methods retrieves the order info"""
        order = {
            "customer_id": self.customer.pk,
            "delivery_address": self.delivery_address,
            "total": self.total
        }
        return order

    def add_order_details(self, order):
        """ This method adds OrderDetail objects
        to the created order
        """
        for product in self.products_in_request:
            order_detail = OrderDetail(
                    product_id=Product.objects.get(pk=product.get('product_id')),
                    order_id=order,
                    quantity=product.get('quantity')
                    )
            order_detail.save()


