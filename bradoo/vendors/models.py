from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=256);
    city = models.CharField(max_length=256, blank=True, null=True);

    # Only one record for a given CNPJ
    cnpj = models.CharField(max_length=18);

    def serialize(self):
        return {
                "name": self.name,
                "CNPJ": self.cnpj,
                "city": self.city, 
                "products": [product.serialize() for product in self.products.all()]
        };

    def get_name(self):
        return self.name;
    
    def remove_city(self):
        self.city = None;
        self.save();


    def update_cnpj(self, cnpj):
        self.cnpj = cnpj;
        self.save();


    def update_name(self, name):
        self.name = name;
        self.save();
