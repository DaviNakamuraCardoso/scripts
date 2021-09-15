from django.urls import path
from .views import all

app_name = "products"

urlpatterns = [
        path("", all, name="all")
]
