from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from warehouse.views import *
from store.views import *

router = routers.SimpleRouter()
router.register(r'stores', OrderViewSet)
router.register(r'warehouses', WarehouseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
