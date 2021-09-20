from django.test import TestCase, Client
from django.shortcuts import reverse
from .models import Product
from .examples import *
from vendors.models import Vendor
from vendors.examples import *

# Create your tests here.

class ProductTest(TestCase):

    def setUp(self):
        v1 = Vendor.objects.create(name="Example", cnpj="77.777.777/0001.777")
        p1 = Product.objects.create(vendor=v1, name="Computer", code=29, price=29.9)
        
    def test_status_code(self):
        c = Client()
        request = c.get(reverse("products:all"))
        self.assertTrue(request.status_code == 200)

class ProductCreate(TestCase):
    def setUp(self):
        self.url = reverse("products:create")

    def test_method(self):
        c = Client();
        requests = [];
        data = json.dumps({})
        requests.append(c.put(self.url, data))
        requests.append(c.get(self.url, data))
        requests.append(c.delete(self.url, data))

        for request in requests: 
            self.assertNotEqual(request.status_code, 200)

class ProductSearch(TestCase):
    def setUp(self):
        self.url = reverse("products:search");
        self.v1 = Vendor.objects.create(name=NAME_EX, cnpj=CNPJ_EX);
        self.p1 = Product.objects.create(name=PNAME_EX, code=CODE_EX);
        self.p2 = Product.objects.create(name=PNAME_EX2, code=CODE_EX2);

    def test_method(self):
        c = Client();
        requests = [];
        data = json.dumps({});
        requests.append(c.put(self.url, data))
        requests.append(c.post(self.url, data))
        requests.append(c.delete(self.url, data))

        for request in requests: 
            self.assertNotEqual(request.status_code, 200);

class ProductUpdate(TestCase):
    def setUp(self):
        self.url = reverse("products:search");
        self.v1 = Vendor.objects.create(name=NAME_EX, cnpj=CNPJ_EX);
        self.p1 = Product.objects.create(name=PNAME_EX, code=CODE_EX);
        self.p2 = Product.objects.create(name=PNAME_EX2, code=CODE_EX2);

    def test_method(self):
        c = Client();
        data = json.dumps({});
        requests = [];
        requests.append(c.get(self.url, data))
        requests.append(c.post(self.url, data))
        requests.append(c.delete(self.url, data))

        for request in requests: 
            self.assertNotEqual(request.status_code, 200);


class ProductDelete(TestCase):
    def setUp(self):
        self.url = reverse("products:search");
        self.v1 = Vendor.objects.create(name=NAME_EX, cnpj=CNPJ_EX);
        self.p1 = Product.objects.create(name=PNAME_EX, code=CODE_EX);
        self.p2 = Product.objects.create(name=PNAME_EX2, code=CODE_EX2);

    def test_method(self):
        c = Client();
        requests = [];
        data = json.dumps({});
        requests.append(c.put(self.url, data))
        requests.append(c.post(self.url, data))
        requests.append(c.get(self.url, data))

        for request in requests: 
            self.assertNotEqual(request.status_code, 200);

