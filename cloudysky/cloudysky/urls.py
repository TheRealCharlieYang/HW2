
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('myapp.urls')),  # Replace 'myapp' with your actual app name
]
