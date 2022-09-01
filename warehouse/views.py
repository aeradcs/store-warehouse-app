from rest_framework.viewsets import ModelViewSet

from .models import Warehouse
from .serializers import WarehouseSerializer


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
