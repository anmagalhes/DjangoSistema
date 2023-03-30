from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

admin.site.site_header = 'Cadastro Intranet'
admin.site.site_title = 'Cadastro Intranet'
admin.site.index_title = 'Cadastro Admin'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('backend.core.urls', namespace='core')),
    path('admin/', admin.site.urls),
]
