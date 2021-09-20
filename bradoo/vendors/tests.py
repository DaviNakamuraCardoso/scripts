from django.test import TestCase, Client, RequestFactory
from django.shortcuts import reverse
from .utils import is_valid_cnpj, is_valid_cnpj_format
from .models import Vendor
from .examples import *
from products.models import Product
import json

# Create your tests here.

class TestVendor(TestCase):
    def setUp(self):
        v1 = Vendor.objects.create(name=NAME_EX, cnpj=CNPJ_EX);

        p1 = Product.objects.create(vendor=v1, name="Computer", code=12, price=77.9);

    def test_serialization(self):
        data = Vendor.objects.get(name=NAME_EX).serialize();
        self.assertTrue(data['name'] == NAME_EX);
        self.assertTrue(data['CNPJ'] == CNPJ_EX);
        self.assertTrue(data['products'][0]['name'] == "Computer");
        self.assertTrue(data['products'][0]['code'] == 12);
        self.assertTrue(data['products'][0]['price'] == 77.9);
        self.assertTrue(len(data['products']) == 1);

        
class TestValidCNPJ(TestCase):
    def setUp(self):
        v1 = Vendor.objects.create(name=NAME_EX, cnpj=CNPJ_EX);

    def test_unique_cnpj_false(self):
        """Test if the cnpj function returns False when given a CNPJ that is already taken"""
        self.assertFalse(is_valid_cnpj(CNPJ_EX));

    def test_unique_cnpj_true(self):
        """Test if the cnpj function returns False when given a CNPJ that is not taken."""
        self.assertTrue(is_valid_cnpj("88.888.888/0001-88"));

    def test_cnpj_format_false(self):
        """Test if the format function returns False for invalid formats""" 
        self.assertFalse(is_valid_cnpj("88.88"));
        self.assertFalse(is_valid_cnpj("88.888.888/9991-88"));
        self.assertFalse(is_valid_cnpj("88.888.888/0001-9"));

    def test_cnpj_format_true(self):
        """Test if the format function returns True for valid formats""" 
        self.assertTrue(is_valid_cnpj("99.999.999/0001-99"));
        self.assertTrue(is_valid_cnpj("99999999000199"));
        self.assertTrue(is_valid_cnpj("99.999999/000199"));



class TestVendorCreation(TestCase):

    def test_creation_ok(self):
        c = Client()

        response = c.post(reverse("vendors:create"), 
                {"name": NAME_EX, "cnpj": CNPJ_EX, "city": CITY_EX});
        response2 = c.post(reverse("vendors:create"),
                {"name": NAME_EX2, "cnpj": CNPJ_EX2});

        self.assertTrue(response.status_code == 200);
        self.assertTrue(response2.status_code == 200);

    def test_creation_fail(self):
        c = Client()

        response = c.post(reverse("vendors:create"),
                {"name": NAME_EX, "cnpj": ""});

        response2 = c.post(reverse("vendors:create"),
                {"name": "", "cnpj": CNPJ_EX});

        self.assertFalse(response.status_code == 200);
        self.assertFalse(response.status_code == 200);


class TestVendorSearches(TestCase):
    def setUp(self):
        self.v1 = Vendor.objects.create(name=NAME_EX, cnpj=CNPJ_EX);
        self.v2 = Vendor.objects.create(name=NAME_EX2, cnpj=CNPJ_EX2);

    def test_search_name(self):
        c = Client();
        response = c.get(reverse("vendors:search"), {"name": NAME_EX});

        match = response.json()[0];

        self.assertTrue(len(response.json()) == 1);
        self.assertTrue(match['name'] == NAME_EX);
        self.assertTrue(match['CNPJ'] == CNPJ_EX);
        self.assertTrue(response.status_code == 200);

    def test_search_name2(self):
        c = Client();
        response = c.get(reverse("vendors:search"), {"name": NAME_EX2});

        match = response.json()[0];

        self.assertTrue(len(response.json()) == 1);
        self.assertTrue(match['name'] == NAME_EX2);
        self.assertTrue(match['CNPJ'] == CNPJ_EX2);
        self.assertTrue(response.status_code == 200);

    def test_search_cnpj(self):
        c = Client();
        response = c.get(reverse("vendors:search"), {"cnpj": CNPJ_EX});

        match = response.json()[0];

        self.assertTrue(len(response.json()) == 1);
        self.assertTrue(match['name'] == NAME_EX);
        self.assertTrue(match['CNPJ'] == CNPJ_EX);
        self.assertTrue(response.status_code == 200);

    def test_search_cnpj2(self):
        c = Client();
        response = c.get(reverse("vendors:search"), {"cnpj": CNPJ_EX2});

        match = response.json()[0];

        self.assertTrue(len(response.json()) == 1);
        self.assertTrue(match['name'] == NAME_EX2);
        self.assertTrue(match['CNPJ'] == CNPJ_EX2);
        self.assertTrue(response.status_code == 200);

    def test_search_wrong_method(self):
        c = Client()
        response = c.post(reverse("vendors:search"), {"cnpj": CNPJ_EX});
        response2 = c.delete(reverse("vendors:search"), {"cnpj": CNPJ_EX});
        response3 = c.put(reverse("vendors:search"), {"cnpj": CNPJ_EX});

        self.assertFalse(response == 200);
        self.assertFalse(response2 == 200);
        self.assertFalse(response3 == 200);

class TestVendorUpdate(TestCase):
    def setUp(self):
        self.v1 = Vendor.objects.create(name=NAME_EX, cnpj=CNPJ_EX);
        self.v2 = Vendor.objects.create(name=NAME_EX2, cnpj=CNPJ_EX2);
        self.url = reverse("vendors:update");

    def test_update_name(self):
        c = Client();
        data = { 
                "name": NAME_EX,
                "new_name": NAME_EX_UPDATED
                }
        response = c.put(self.url, json.dumps(data));

        self.assertEqual(response.status_code, 200);
        
        # Update the field pointer
        self.v1 = Vendor.objects.get(pk=self.v1.id);
        self.assertEqual(self.v1.name, NAME_EX_UPDATED); 
       

    def test_update_name2(self):
        c = Client();
        data = {
                "CNPJ": CNPJ_EX2,
                "new_name": NAME_EX2_UPDATED
                }
        response = c.put(self.url, json.dumps(data));

        self.assertEqual(response.status_code, 200);

        self.v2 = Vendor.objects.get(pk=self.v2.id);
        self.assertEqual(self.v2.name, NAME_EX2_UPDATED);
    
    def test_update_cnpj(self):
        c = Client();
        data = {
                "id": self.v1.id,
                "new_CNPJ": CNPJ_EX_UPDATED 
        }
        response = c.put(self.url, json.dumps(data));
        
        self.assertEqual(response.status_code, 200);
        self.v1 = Vendor.objects.get(pk=self.v1.id);

        self.assertEqual(self.v1.cnpj, CNPJ_EX_UPDATED);

    def test_update_name_false(self):
        c = Client();
        data = {
                "id": ID_EX_DOESNOTEXIST,
                "new_name": NAME_EX_UPDATED
                }
        data2 = {
                "name": NAME_EX_DOESNOTEXIST,
                "new_name": NAME_EX_UPDATED
                }
        data3 = {
                "cnpj": CNPJ_EX_DOESNOTEXIST,
                "new_name": NAME_EX_UPDATED
                }
        response = c.put(self.url, json.dumps(data));

        self.assertNotEqual(response.status_code, 200);

    def test_update_cnpj_false(self):
        """Test Vendor 1 trying to get Vendor's 2 CNPJ"""
        c = Client();
        data = {
                "id": self.v1.id, 
                "new_CNPJ": self.v2.cnpj
                }

        response = c.put(self.url, json.dumps(data));

        self.v1 = Vendor.objects.get(pk=self.v1.id);
        self.assertNotEqual(response.status_code, 200);
        self.assertNotEqual(self.v1.cnpj, self.v2.cnpj);
        
class TestDelete(TestCase):
    def setUp(self):
        self.url = reverse("vendors:delete");
        self.v1 = Vendor.objects.create(name=NAME_EX, cnpj=CNPJ_EX);
        self.v2 = Vendor.objects.create(
                name=NAME_EX2, 
                cnpj=CNPJ_EX2,
                city=CITY_EX

                );

    def test_delete_invalid(self):
        c = Client();

        data = {
            "id": self.v1.id,
            "field": "name"
            };
        response = c.delete(self.url, json.dumps(data));


        self.v1 = Vendor.objects.get(pk=self.v1.id);
        self.assertNotEqual(response.status_code, 200);
        self.assertEqual(self.v1.name, NAME_EX);

    def test_delete_city(self):
        c = Client();
        data = {
            "id": self.v2.id,
            "field": "city"
            };
        
        response = c.delete(self.url, json.dumps(data));
        self.v2 = Vendor.objects.get(pk=self.v2.id);
        self.assertEqual(response.status_code, 200);
        self.assertEqual(self.v2.city, None);

    def test_delete_vendor(self):
        c = Client();
        data = {
            "id": self.v1.id,
            "field": "vendor"
        };
        response = c.delete(self.url, json.dumps(data));

        b = False;
        try: 
            self.v1 = Vendor.objects.get(pk=self.v1.id);
        except Vendor.DoesNotExist: 
            b = True;

        self.assertTrue(b);



        

        
