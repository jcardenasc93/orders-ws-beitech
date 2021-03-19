from django.contrib import admin
from orders.models import Product, Customer, Order, OrderDetail
# Register your models here.
app_models = [Product, Customer, Order, OrderDetail]
admin.site.register(app_models)

