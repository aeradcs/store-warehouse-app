import requests
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework import status

from store.models import Order
from store.views import OrderViewSet


@receiver(post_save, sender=Order)
def post_save_listener(**kwargs):
    print("ORD POST========")
    if kwargs['created']:
        data = kwargs['instance'].to_dict()

        url = "http://localhost:8001/warehouses/"
        body = {"order_name": data["order_name"], "status": data["status"],
                "warehouse": data["warehouse"], "store": data["store"]}

        response = requests.post(url=url, json=body)
        status_code = response.status_code
        if not status_code == status.HTTP_201_CREATED:
            raise Exception("Something went wrong while Store-Warehouse synchronization.",
                            status.HTTP_500_INTERNAL_SERVER_ERROR)


def equal(old_instance, instance):
    for v1, v2 in zip(old_instance.values(), instance.values()):
        if not v1 == v2:
            return False
    return True


@receiver(pre_save, sender=Order)
def pre_save_listener(**kwargs):
    print("ORD PRE========")
    instance = kwargs['instance']
    pk = instance.id
    print('ORD PRE instance', instance.to_dict())
    if pk is not None:
        old_instance = Order.objects.get(pk=pk).to_dict()
        print('ORD PRE old_instance', old_instance)
        instance = instance.to_dict()

        if not equal(old_instance, instance):

            OrderViewSet.put()
            url = f"http://localhost:8001/warehouses/"
            body = {"old": old_instance, "new": instance}

            try:
                response = requests.patch(url=url, json=body)
                status_code = response.status_code
                print("status_code", status_code)
                if not status_code == status.HTTP_200_OK:
                    raise Exception("Something went wrong while Store-Warehouse synchronization.",
                                    status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Exception as e:
                print(e)
