import requests
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework import status

from warehouse.models import Warehouse
def equal(old_instance, instance):
    for v1, v2 in zip(old_instance.values(), instance.values()):
        if not v1 == v2:
            return False
    return True


# @receiver(pre_save, sender=Warehouse)
# def pre_save_listener(**kwargs):
#     print("WARE PRE=======================")
#     instance = kwargs['instance']
#     pk = instance.id
#     print('WARE PRE instance', instance.to_dict())
#     if pk is not None:
#         old_instance = Warehouse.objects.get(pk=pk).to_dict()
#         print('WARE PRE old_instance', old_instance)
#         instance = instance.to_dict()
#         if not equal(old_instance, instance):
#             url = f"http://localhost:8001/stores/"
#             body = {"old": old_instance, "new": instance}
#
#             try:
#                 response = requests.patch(url=url, json=body)
#                 status_code = response.status_code
#                 print("status_code", status_code)
#                 if not status_code == status.HTTP_200_OK:
#                     raise Exception("Something went wrong while Store-Warehouse synchronization.",
#                                     status.HTTP_500_INTERNAL_SERVER_ERROR)
#             except Exception as e:
#                 print(e)