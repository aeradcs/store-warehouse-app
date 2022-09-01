import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models import Order
from storeWarehouse.utils.requests_sender import *
from storeWarehouse.utils.dict_utils import *


@receiver(post_save, sender=Order)
def post_save_listener(**kwargs):
    if kwargs['created']:
        order_instance = kwargs['instance'].to_dict()
        url = "http://localhost:8001/warehouses/"
        send_post(url, order_instance)

    else:
        order_instance = kwargs['instance'].to_dict()
        url = "http://localhost:8001/warehouses/"
        response = requests.get(url=url)

        warehouses_from_db = json.loads(response.content)
        warehouse_id, warehouse = get_id_by_unique_identifier(warehouses_from_db, order_instance['object_id'])

        if not equal(warehouse, order_instance):
            url = f"http://localhost:8001/warehouses/{warehouse_id}/"
            send_put(url, order_instance)
