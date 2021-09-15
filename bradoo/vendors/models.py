from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=256);
    city = models.CharField(max_length=256);

    # Only one record for a given CNPJ
    cnpj = models.CharField(max_length=18);

    def serialize(self):
        return {
                "name": self.name,
                "CNPJ": self.cnpj,
                "city": self.city, 
                "products": [product.serialize() for product in self.products.all()]
        };

