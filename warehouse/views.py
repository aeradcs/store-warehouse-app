from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from storeWarehouse.utils.http import get_body_attr_or_replace
from .models import Warehouse
from .serializers import WarehouseSerializer
from rest_framework import mixins

class WarehouseViewSet(viewsets.ViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        instance = Warehouse.objects.get(pk=pk)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
