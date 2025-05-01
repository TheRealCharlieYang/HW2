from django.urls import path
from . import views
app_name = 'app'
urlpatterns = [
    path("dummypage", views.dummypage, name="dummypage"),
    path("time", views.get_time, name="get_time"),
    path("sum", views.get_sum, name="get_sum"),
    path('', views.index, name='index'),              
    path('new/', views.new_user_form, name='new_user'),
    path('createUser/', views.create_user, name='create_user'),  
]
