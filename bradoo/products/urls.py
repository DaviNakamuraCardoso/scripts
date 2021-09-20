from django.urls import path
from .views import all, create, search, update, delete

app_name = "products"

urlpatterns = [
        path("", all, name="all"),
        path("create", create, name="create"),
        path("search", search, name="search"),
        path("update", update, name="update"),
        path("delete", delete, name="delete")
]
