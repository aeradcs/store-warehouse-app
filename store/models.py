from django.db import models
from storeWarehouse.utils.order_statuses import STATUS_CHOICES


class Order(models.Model):
    object_id = models.BigIntegerField()
    order_name = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    warehouse = models.TextField()
    store = models.TextField()

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        try:
            Order.objects.get(object_id=self.object_id)
        except Exception:
            self.object_id = id(self)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.object_id} {self.order_name} {self.status} {self.warehouse} {self.store}"

    def to_dict(self):
        return {"object_id": self.object_id, "order_name": self.order_name, "status": self.status, "warehouse": self.warehouse, "store": self.store}

