""" Models serializers """
from orders.models import Order, OrderDetail
from rest_framework import serializers


class OrderDetailSerializer(serializers.ModelSerializer):
    """OrderDetail model serializer"""
    product_name = serializers.CharField(source='product_id.name',
                                         read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['product_name', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    """Order model serializer"""
    order_details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'order_id', 'customer_id', 'creation_date', 'total',
            'delivery_address', 'order_details'
        ]
