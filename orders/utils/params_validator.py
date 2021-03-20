""" Query parameters validator """
from datetime import datetime


def validate_query_params(request: dict):
    """ This method access to the request dict and
    validates thar the start_date and end_date params
    be present and with correct values
    Args:
        request (dict): The incoming URL dictionary
    Returns:
        start_date (datetime): Start date in datetime format
        end_date (datetime): End date in datetime format
        None if cannot format the params values
    """
    try:
        start_date = datetime.strptime(request['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request['end_date'], '%Y-%m-%d')
    except:
        return None
    else:
        dates = {
            "start_date": request['start_date'],
            "end_date": request['end_date']
        }
        return dates
