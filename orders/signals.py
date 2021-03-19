from django.db.models.signals import pre_save
from django.dispatch import receiver
from orders.models import OrderDetail

@receiver(pre_save, sender=OrderDetail)
def pre_save_order_detail(sender, instance, **kwargs):
    """ This method fetchs current product data to
    adds in the OrderDetail object
    """
    instance.price = instance.product_id.price
    instance.product_description = instance.product_id.product_description

