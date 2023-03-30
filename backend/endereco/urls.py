from django.urls import include, path

from backend.endereco import views as v

app_name = 'endereco'


endereco_urlpatterns = [
    path('', v.endereco_list, name='endereco_list'),
    path('create/', v.EnderecoCreateView.as_view(), name='endereco_create'),  # noqa E501
]


urlpatterns = [
    path('', include(endereco_urlpatterns)),
]
