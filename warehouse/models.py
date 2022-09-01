from django.db import models
from storeWarehouse.utils.order_statuses import STATUS_CHOICES


class Warehouse(models.Model):
    object_id = models.BigIntegerField()
    order_name = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    warehouse = models.TextField()
    store = models.TextField()

    def __str__(self):
        return f"{self.object_id} {self.order_name} {self.status} {self.warehouse} {self.store}"

    def to_dict(self):
        return {"object_id": self.object_id, "order_name": self.order_name, "status": self.status,
                "warehouse": self.warehouse, "store": self.store}
