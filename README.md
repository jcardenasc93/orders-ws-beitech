# Order REST Web Service
This project conatins the develop of the tech test for python developer position at Beitech SAS
## Tech Requirements
* python 3.8
* pipenv (To install it just run `pip install pipenv`)
* Django 3.1
* SQLite
## Steps to launch the project
To launch the project just follow the next steps:
1. Clone the repo
2. Run `cd orders-ws-beitech && pipenv install` this command will install the required packages
3. Copy `.env.example` file to `.env` and adjust your environment variables
4. Create the `DJANGO_SECRET_KEY` with the following command `python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'`
5. Activate the virtual environment wiht `pipenv shell`
6. Apply migrations to your database with `python manage.py migrate`
7. Finally just run `python manage.py runserver` and the app will be serve in your `localhost` on port `8000`
### Load initial data
This project implements a mechanism to load initial data for the `Product`, `Customer` and `CustomerProduct` models. To load initial data into the database run:
```bash
python manage.py loaddata orders/initial_data.yaml
```
At this moment your SQLite database should contains some records on the `product`, `customer` and `customer_product` tables

