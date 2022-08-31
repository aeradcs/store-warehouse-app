from django.db import models
from storeWarehouse.utils.order_statuses import STATUS_CHOICES


class Order(models.Model):
    order_name = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    warehouse = models.TextField()
    store = models.TextField()

    class Meta:
        unique_together = ('order_name', 'warehouse', 'store',)

    def __str__(self):
        return f"{self.order_name} {self.status} {self.warehouse} {self.store}"
