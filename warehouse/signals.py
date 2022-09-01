import json

import requests
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework import status
from .serializers import *
from store.models import Order
from storeWarehouse.utils.equality import equal
@receiver(post_save, sender=Warehouse)
def post_save_listener(**kwargs):


    print(kwargs)

    if not kwargs['created']:
        data = kwargs['instance'].to_dict()
        url = "http://localhost:8000/stores/"
        response = requests.get(url=url)
        jsn = json.loads(response.content)
        for row in jsn:
            if row['object_id'] == data['object_id']:
                id = row['id']
                del row['id']
                print("Warehouse row", row)
                print("Warehouse data", data)
                print("Warehouse warehouse in db", Warehouse.objects.get(object_id=row['object_id']).to_dict())

                if not equal(row, data):
                    print("Warehouse not equal")
                    url = f"http://localhost:8000/stores/{id}/"
                    response = requests.put(url=url, json=data)
                    status_code = response.status_code
                    if not status_code == status.HTTP_200_OK:
                        raise Exception("Something went wrong while Warehouse-Store synchronization.",
                                        status.HTTP_500_INTERNAL_SERVER_ERROR)



    # if not kwargs['created']:
    #     data = kwargs['instance'].to_dict()
    #     url = "http://localhost:8000/stores/"
    #     response = requests.get(url=url)
    #     jsn = json.loads(response.content)
    #     print("jsn", jsn)
    #     for row in jsn:
    #         if row['object_id'] == data['object_id']:
    #             id = row['id']
    #
    #             url = f"http://localhost:8000/stores/{id}/"
    #             response = requests.put(url=url, json=data)
    #             status_code = response.status_code
    #             print(status_code)
    #             if not status_code == status.HTTP_200_OK:
    #                 raise Exception("Something went wrong while Store-Warehouse synchronization.",
    #                                 status.HTTP_500_INTERNAL_SERVER_ERROR)
    #
    #
