from django.urls import path
from . import views

urlpatterns = [
    path("dummypage", views.dummypage, name="dummypage"),
    path("time", views.get_time, name="get_time"),
    path("sum", views.get_sum, name="get_sum"),
]
