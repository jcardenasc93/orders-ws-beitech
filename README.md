# Order REST Web Service
This project conatins the develop of the tech test for python developer position at Beitech SAS

## E/R Model

This is the entity-relationship model defined for the solution

![er-model](https://github.com/jcardenasc93/orders-ws-beitech/blob/main/images/ER_model.png)

### SQL script to create database

This is the [file](https://github.com/jcardenasc93/orders-ws-beitech/blob/main/create_db.sql) with the SQL script to crate the project database. **IMPORTANT:** You can run this script but as this is a Django project I suggest to check [this](#steps) to create the database

## Tech Requirements
* [python 3.8](https://www.python.org/downloads/release/python-388/)
* [pipenv](https://pipenv.pypa.io/en/latest/) (To install it just run `pip3 install pipenv`)
* [Django 3.1](https://www.djangoproject.com/download/)
* [PostgreSQL 10](https://www.postgresql.org/download/) or higher, [SQLite](https://sqlite.org/download.html).
* [apidoc](https://apidocjs.com/#install)
## <a name="steps"></a>Steps to launch the project

To launch the project just follow the next steps:
1. Clone the repo
2. Run `cd orders-ws-beitech && pipenv install` this command will install the required packages
3. Copy `.env.example` file to `.env` and adjust your environment variables values
4. Create the `DJANGO_SECRET_KEY` with the following command `python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'`
5. Activate the virtual environment with `pipenv shell`
6. Create database and apply migrations to it with `python manage.py migrate`
7. Finally just run `python manage.py runserver` and the app will be serve in your `localhost` on port `8000`
### Load initial data
This project implements a mechanism to load initial data for the `Product`, `Customer` and `CustomerProduct` models. To load initial data into the database run:
```bash
python manage.py loaddata orders/initial_data.yaml
```
At this moment your SQLite database should contains some records on the `product`, `customer` and `customer_product` tables. If you need to change initial data values you can edit this [file](https://github.com/jcardenasc93/orders-ws-beitech/blob/main/orders/initial_data.yaml).

## API Documentation

The API documentation is auto-generated with [apidoc](https://apidocjs.com/#install). Once you have installed the package inside the root directory of the project just run `apidoc -i. -o docs/`, this command will create a `docs/` directory with documentation files inside. Then just open the file `index.html` in a browser to see the API documentation



