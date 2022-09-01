# Store Warehouse App

Project contains two apps - **store** and **warehouse**. 

Apps communicate via http requests. Apps have separate sqlite3 databases.

When change is made in one database, e.g. new order is created in the store or order status is changed in warehouse, the change synchronize in another database as well.

## Enviroment

- Python
- Django

## Installation

`git clone https://github.com/aeradcs/store-warehouse-app.git`

`cd store-warehouse-app/`

`sudo apt install python3.10-venv`

`python3 -m venv venv`

`pip install -r requirements.txt`

`python3 manage.py makemigrations store && python3 manage.py makemigrations warehouse && python3 manage.py migrate --database=store && python3 manage.py migrate --database=warehouse && python3 manage.py migrate`

`python3 manage.py runserver`

**In another terminal:**

`cd Desktop/store-warehouse-app/`

`python3 manage.py runserver 8001`


## Usage

Open [http://127.0.0.1:8000/stores/](http://127.0.0.1:8000/stores/) and [http://127.0.0.1:8001/warehouses/](http://127.0.0.1:8001/warehouses/) in a browser and you'll see Django forms for communicating with apps. 

You can:
- get lists of orders in store and warehouse

- get order by id in store and warehouse

- create new order in store

- change order's info in store and warehouse
