from django.urls import path
from .views import index
from . import views

app_name = 'alarm'

urlpatterns = [
    path("", views.index, name="index"),
    path("time_register", views.time_register),
    path("time_list", views.time_list),
    path("timeAjax/", views.index),
]