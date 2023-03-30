from django.urls import include, path

from backend.fornecedor import views as v

app_name = 'fornecedor'


fornecedor_urlpatterns = [
    path('', v.fornecedor_list, name='fornecedor_list'),
]


urlpatterns = [
    path('', include(fornecedor_urlpatterns)),
]
