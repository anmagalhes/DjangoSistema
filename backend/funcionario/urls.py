from django.urls import include, path

from backend.funcionario import views as v

app_name = 'funcionario'


documento_urlpatterns = [
    path('', v.documento_list, name='documento_list'),
    path('create/', v.DocumentoCreateView.as_view(), name='documento_create'),
]

funcionario_urlpatterns = [
    path('', v.funcionario_list, name='funcionario_list'),
    path('create/', v.FuncionarioCreateView.as_view(), name='funcionario_create'),
]

hora_extra_urlpatterns = [
    path('', v.hora_extra_list, name='hora_extra_list'),
    path('create/', v.HoraExtraFuncionarioCreateView.as_view(), name='hora_extra_create'),
]


urlpatterns = [
    path('documento/', include(documento_urlpatterns)),
    path('funcionario/', include(funcionario_urlpatterns)),
    path('hora-extra/', include(hora_extra_urlpatterns)),
]
