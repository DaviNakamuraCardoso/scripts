from django.db import models
from vendors.models import Vendor

# Create your models here.

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="products") 
    name = models.CharField(max_length=256)
    code = models.IntegerField()
    price = models.FloatField(blank=True, null=True)

    def serialize(self):
        return {
            "name": self.name,
            "code": self.code,
            "price": self.price
        }


