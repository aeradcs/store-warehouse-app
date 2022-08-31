import copy

import requests
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Warehouse
from .serializers import WarehouseSerializer
from rest_framework import mixins
from django.db.models import Q


class WarehouseViewSet(viewsets.ViewSet,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def create(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # url = "http://localhost:8001/warehouses/"
        # body = {"order_name": data["order_name"], "status": data["status"], "store": "default"}
        #
        # response = requests.post(url=url, json=body)
        # status_code = response.status_code
        # if not status_code == status.HTTP_201_CREATED:
        #     raise Exception("Something went wrong while Store-Warehouse synchronization.",
        #                     status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['patch'], detail=True)
    def patch(self, request):
        print("WAREH PATCH")

        data = request.data
        old = data['old']
        new = data['new']
        print(old)
        print(new)

        instance = Warehouse.objects.get(order_name=old['order_name'], warehouse=old['warehouse'], store=old['store'])
        print(instance)
        serializer = self.get_serializer(data=new)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, new)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True)
    def put(self, request, pk=None):
        print("WAREH PUT")

        instance = Warehouse.objects.get(pk=pk)
        old_instance = copy.deepcopy(instance)
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, data)

        print(old_instance)
        print(instance)
        url = f"http://localhost:8000/stores/"
        body = {"old": {"order_name": old_instance.order_name, "status": old_instance.status,
                        "warehouse": old_instance.warehouse, "store": old_instance.store},
                "new": {"order_name": instance.order_name, "status": instance.status,
                        "warehouse": instance.warehouse, "store": instance.store}}
        try:
            response = requests.patch(url=url, json=body)
            status_code = response.status_code
            print(status_code)
            if not status_code == status.HTTP_200_OK:
                raise Exception("Something went wrong while Store-Warehouse synchronization.",
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(e)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # def update(self, request, pk=None):
    #     data = request.data
    #     instance = Warehouse.objects.get(pk=pk)
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.update(instance, data)
    #
    #
    #     # url = f"http://localhost:8000/stores/{str(pk)}/"
    #     # body = {"order_name": data["order_name"], "status": data["status"], "store": "1"}
    #     #
    #     # response = requests.put(url=url, json=body)
    #     # status_code = response.status_code
    #     # if not status_code == status.HTTP_200_OK:
    #     #     raise Exception("Something went wrong while Store-Warehouse synchronization.",
    #     #                     status.HTTP_500_INTERNAL_SERVER_ERROR)
    #
    #     return Response(serializer.data, status=status.HTTP_200_OK)
