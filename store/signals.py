import json

import requests
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework import status
from .serializers import *
from store.models import Order

@receiver(post_save, sender=Order)
def post_save_listener(**kwargs):
    if kwargs['created']:

        data = kwargs['instance'].to_dict()

        url = "http://localhost:8001/warehouses/"

        response = requests.post(url=url, json=data)
        status_code = response.status_code
        if not status_code == status.HTTP_201_CREATED:
            raise Exception("Something went wrong while Store-Warehouse synchronization.",
                            status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        data = kwargs['instance'].to_dict()
        url = "http://localhost:8001/warehouses/"
        response = requests.get(url=url)
        jsn = json.loads(response.content)
        for row in jsn:
            if row['object_id'] == data['object_id']:
                id = row['id']

                url = f"http://localhost:8001/warehouses/{id}/"
                response = requests.put(url=url, json=data)
                status_code = response.status_code
                if not status_code == status.HTTP_200_OK:
                    raise Exception("Something went wrong while Store-Warehouse synchronization.",
                                    status.HTTP_500_INTERNAL_SERVER_ERROR)

