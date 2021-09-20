from django.urls import path
from .views import create, all, search, update, delete

app_name = "vendors"

urlpatterns = [
    path("create", create, name="create"), 
    path("search", search, name="search"),
    path("update", update, name="update"),
    path("delete", delete, name="delete"),
    path("", all, name="all")
]
