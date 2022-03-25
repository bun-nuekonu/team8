from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path("", views.index,),
    path("time_register", views.time_register),
    path("time_list", views.time_list),
]