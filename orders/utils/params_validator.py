""" Query parameters validator """
from datetime import datetime
from orders.models import Customer


def validate_query_params(request: dict, customer_id):
    """ This method access to the request dict and
    validates thar the start_date and end_date params
    be present and with correct values
    Args:
        request (dict): The incoming URL dictionary
        customer_id: The primary key for the customer
    Returns:
        start_date (datetime): Start date in datetime format
        end_date (datetime): End date in datetime format
        customer (Customer): The retrieved Customer object
        None if cannot format the params values
    """
    try:
        start_date = datetime.strptime(request['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request['end_date'], '%Y-%m-%d')
        customer = Customer.objects.get(pk=customer_id)
    except:
        return None
    else:
        if customer:
            data = {
                "start_date": request['start_date'],
                "end_date": request['end_date'],
                "customer": customer
            }
            return data
        else:
            return None
