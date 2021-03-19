from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'

    # Adds signals setup
    def ready(self):
        import orders.signals
