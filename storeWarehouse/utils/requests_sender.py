import requests
from rest_framework import status


def send_post(url, data):
    response = requests.post(url=url, json=data)
    status_code = response.status_code
    if not status_code == status.HTTP_201_CREATED:
        raise Exception("Something went wrong while Store-Warehouse synchronization.",
                        status.HTTP_500_INTERNAL_SERVER_ERROR)


def send_put(url, instance):
    response = requests.put(url=url, json=instance)
    status_code = response.status_code
    if not status_code == status.HTTP_200_OK:
        raise Exception("Something went wrong while Store-Warehouse synchronization.",
                        status.HTTP_500_INTERNAL_SERVER_ERROR)
