from django.urls import include, path

from backend.cliente import views as v

app_name = 'cliente'


cliente_urlpatterns = [
    path('', v.cliente_list, name='cliente_list'),
    path('create/', v.ClienteCreateView.as_view(), name='cliente_create'),
]


urlpatterns = [
    path('', include(cliente_urlpatterns)),
]
