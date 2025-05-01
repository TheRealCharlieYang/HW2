from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app.views import index

urlpatterns = [
    path('',            index, name='root_index'),      # GET  /
    path('index.html',  index, name='index_html'),      # GET  /index.html

    path('admin/',      admin.site.urls),
    path('app/',        include('app.urls')),

    # login/logout:
    path('login/',          auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('logout/',         auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
