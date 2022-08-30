from django.db import models
from storeWarehouse.utils.order_statuses import STATUS_CHOICES


class Warehouse( models.Model):
    order_name = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    store = models.TextField()

    def __str__(self):
        return self.order_name + " " + self.status + " " + self.store
