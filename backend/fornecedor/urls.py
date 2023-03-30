from django.urls import include, path

from backend.fornecedor import views as v

app_name = 'fornecedor'


fornecedor_urlpatterns = [
    path('', v.fornecedor_list, name='fornecedor_list'),
    path('create/', v.FornecedorCreateView.as_view(), name='fornecedor_create'),
]


urlpatterns = [
    path('', include(fornecedor_urlpatterns)),
]
