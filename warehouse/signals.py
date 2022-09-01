import json
import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from storeWarehouse.utils.dict_utils import equal, get_id_by_unique_identifier
from storeWarehouse.utils.requests_sender import send_put
from warehouse.models import Warehouse


@receiver(post_save, sender=Warehouse)
def post_save_listener(**kwargs):
    if not kwargs['created']:
        warehouse_instance = kwargs['instance'].to_dict()
        url = "http://localhost:8001/stores/"
        response = requests.get(url=url)

        orders_from_db = json.loads(response.content)
        order_id, order = get_id_by_unique_identifier(orders_from_db, warehouse_instance['object_id'])

        if not equal(order, warehouse_instance):
            url = f"http://localhost:8001/stores/{order_id}/"
            send_put(url, warehouse_instance)
