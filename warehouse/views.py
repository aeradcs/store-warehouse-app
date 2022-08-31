import copy

import requests
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Warehouse
from .serializers import WarehouseSerializer
from rest_framework import mixins


class WarehouseViewSet(viewsets.ViewSet,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.CreateModelMixin,
                       GenericViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    @action(methods=['patch'], detail=True)
    def patch(self, request):
        print("WAREH PATCH")

        data = request.data
        old = data['old']
        new = data['new']

        instance = Warehouse.objects.get(order_name=old['order_name'], warehouse=old['warehouse'], store=old['store'])
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