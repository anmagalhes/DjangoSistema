from django.urls import include, path

from backend.endereco import views as v

app_name = 'endereco'


endereco_urlpatterns = [
    path('', v.endereco_list, name='endereco_list'),
    path('create/', v.EnderecoCreateView.as_view(), name='endereco_create'),  # noqa E501
    path('<int:pk>/update/', v.EnderecoUpdateView.as_view(), name='endereco_update'),
]


urlpatterns = [
    path('', include(endereco_urlpatterns)),
]
