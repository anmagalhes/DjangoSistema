from django.contrib import admin
from django.urls import path


admin.site.site_header = "Cadastro Intranet"
admin.site.site_title = "Cadastro Intranet"
admin.site.index_title = "Cadastro Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
]
