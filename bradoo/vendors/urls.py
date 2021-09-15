from django.urls import path
from .views import create, all 

app_name = "vendors"

urlpatterns = [
    path("create/", create, name="create"), 
    path("", all, name="all")
]
