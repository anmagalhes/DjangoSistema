from django.urls import include, path

from backend.funcionario import views as v

app_name = 'funcionario'


documento_urlpatterns = [
    path('', v.documento_list, name='documento_list'),
    path('create/', v.DocumentoCreateView.as_view(), name='documento_create'),
    path('<int:pk>/update/', v.DocumentoUpdateView.as_view(), name='documento_update'),
]

funcionario_urlpatterns = [
    path('', v.funcionario_list, name='funcionario_list'),
    path('create/', v.FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('<int:pk>/update/', v.FuncionarioUpdateView.as_view(), name='funcionario_update'),
]

hora_extra_urlpatterns = [
    path('', v.hora_extra_list, name='hora_extra_list'),
    path('create/', v.HoraExtraFuncionarioCreateView.as_view(), name='hora_extra_create'),
    path('<int:pk>/update/', v.HoraExtraFuncionarioUpdateView.as_view(), name='hora_extra_update'),
]


urlpatterns = [
    path('documento/', include(documento_urlpatterns)),
    path('funcionario/', include(funcionario_urlpatterns)),
    path('hora-extra/', include(hora_extra_urlpatterns)),
]
