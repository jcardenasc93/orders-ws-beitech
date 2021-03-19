""" orders models definitions """
from django.db import models

# Create your models here.

CHAR_MAX_LENGTH = 191


class Product(models.Model):
    """ Product model definition """
    product_id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=CHAR_MAX_LENGTH)
    product_description = models.CharField(max_length=CHAR_MAX_LENGTH)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_id}- {self.name}"
    class Meta:
        db_table = 'product'


class Customer(models.Model):
    """ Customer model definition """
    customer_id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=CHAR_MAX_LENGTH)
    email = models.EmailField(max_length=CHAR_MAX_LENGTH, unique=True)

    def __str__(self):
        return f"{self.customer_id}- {self.email}"

    class Meta:
        db_table = 'customer'


class CustomerProduct(models.Model):
    """ CustumerProduct intermediate table definition """
    customer_product_id = models.AutoField(auto_created=True, primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'customer_product'
        # Adds compose unique restriction
        unique_together = (('product_id'), ('customer_id'))


class Order(models.Model):
    """ Order model definition """
    order_id = models.AutoField(auto_created=True, primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.CharField(max_length=CHAR_MAX_LENGTH)
    total = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.order_id}- {self.creation_date}"

    class Meta:
        db_table = 'order'


class OrderDetail(models.Model):
    """ Order detail model definition """
    order_detail_id = models.AutoField(auto_created=True, primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_description = models.CharField(max_length=CHAR_MAX_LENGTH, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    quantity = models.IntegerField(max_length=999999999)

    class Meta:
        db_table = 'order_detail'
