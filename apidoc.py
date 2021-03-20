# File with API documentation
"""
@api {get} /orders/customer/:customerId?start_date=AAAA-MM-DD&end_date=AAAA-MM-DD
@apiName GetCustomerOrders
@apiGroup Orders
@apiVersion 0.0.0
@apiDescription List the customer orders filtered by the specified date range

@apiParam (Query String Param)  {String}    start_date      oldest date to filter in format AAAA-MM-DD
@apiParam (Query String Param)  {String}    end_date        most recent date to filter in format AAAA-MM-DD
@apiParamExample    {String}    start_date:
                    2021-03-20
@apiSuccessExample {json}   Success-Response:
    HTTP/1.1 200 OK
    [
        {
            "order_id": 1,
            "customer_id": 1,
            "creation_date": "2021-03-19",
            "total": "4001.98",
            "delivery_address": "avenida siempre viva 123",
            "order_details": [
                {
                    "product_name": "Computer",
                    "quantity": 2
                }
            ]
        }
    ]

@apiErrorExample {String} Invalid-parameters:
    HTTP/1.1 400 BAD_REQUEST
    "Invalid request. Please check filter criteria"
"""

"""
@api {post} /orders/customer/:customerId
@apiName PostCustomerOrders
@apiGroup Orders
@apiVersion 0.0.0
@apiDescription Create customer order

@apiParam (Body Param)  {String}    delivery_address    Customer's delivery address
@apiParam (Body Param)  {json}      products            Products and its quantities included in the order
@apiParamExample    {json}    products:
                      "products": [
                        {
                          "product_id": 1,
                          "quantity": 1
                        },
                        {
                          "product_id": 3,
                          "quantity": 2
                        }
                      ]
@apiSuccessExample {json}   Success-Response:
    HTTP/1.1 200 OK
    {
        "order_id": 4,
        "customer_id": 1,
        "creation_date": "2021-03-20",
        "total": "3300.99",
        "delivery_address": "avenida siempre viva 123",
        "order_details": [
            {
                "product_name": "Computer",
                "quantity": 1
            },
            {
                "product_name": "Camera",
                "quantity": 2
            }
        ]
    }

@apiErrorExample {String}   User not found:
    HTTP/1.1 400 BAD_REQUEST
    "User not found"
@apiErrorExample {String}   Invalid customer products:
    HTTP/1.1 400 BAD_REQUEST
    "Customer cannot order these products"
"""
