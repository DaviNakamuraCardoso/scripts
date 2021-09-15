from django.test import TestCase
from .utils import is_valid_cnpj
from .models import Vendor
from products.models import Product

# Create your tests here.

CNPJ_EX = "77.777.777/0001.77";
NAME_EX = "Example";

class TestVendor(TestCase):
    def setUp(self):
        v1 = Vendor.objects.create(name=NAME_EX, cnpj=CNPJ_EX);

        p1 = Product.objects.create(vendor=v1, name="Computer", code=12, price=77.9);

    def test_serialization(self):
        data = Vendor.objects.get(name=NAME_EX).serialize();
        self.assertTrue(data['name'] == NAME_EX);
        self.assertTrue(data['CNPJ'] == CNPJ_EX);
        self.assertTrue(len(data['products']) == 1);

        
class TestValidCNPJ(TestCase):
    def setUp(self):
        v1 = Vendor.objects.create(name=NAME_EX, cnpj=CNPJ_EX);

    def test_unique_cnpj_false(self):
        """Test if the cnpj function returns False when given a CNPJ that already exists"""
        self.assertFalse(is_valid_cnpj(CNPJ_EX));

    def test_unique_cnpj_true(self):
        """Test if the cnpj function returns False when given a CNPJ that does not exist."""
        self.assertTrue(is_valid_cnpj("88.888.888/0001.88"));


    

