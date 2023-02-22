# from django.contrib import admin
from django.urls import path
from .views import home

# admin.site.site_header = "Login Intranet"
# admin.site.site_title = "Login Intranet"
# admin.site.index_title = "Login Usuarios"

urlpatterns = [
    path(
        '',
        home,
        name='home',
    ),
]
