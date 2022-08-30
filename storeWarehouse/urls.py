from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from warehouse.views import WarehouseViewSet
from store.views import OrderViewSet

router = routers.SimpleRouter()
router.register(r'warehouses', WarehouseViewSet)
router.register(r'stores', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
