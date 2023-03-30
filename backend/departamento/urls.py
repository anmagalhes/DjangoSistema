from django.urls import include, path

from backend.departamento import views as v

app_name = 'departamento'


departamento_urlpatterns = [
    path('', v.departamento_list, name='departamento_list'),
    path('create/', v.DepartamentoCreateView.as_view(), name='departamento_create'),  # noqa E501
    path('<int:pk>/update/', v.DepartamentoUpdateView.as_view(), name='departamento_update'),  # noqa E501
]


urlpatterns = [
    path('', include(departamento_urlpatterns)),
]
