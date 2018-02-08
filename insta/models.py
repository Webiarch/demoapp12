from django.db import models

class CustomerMaster(models.Model):
    Price = models.IntegerField()

    def __str__(self):
        return self.Price
