from django.urls import include, path

from backend.funcionario import views as v

app_name = 'funcionario'


documento_urlpatterns = [
    path('', v.documento_list, name='documento_list'),
]

funcionario_urlpatterns = [
    path('', v.funcionario_list, name='funcionario_list'),
]

hora_extra_urlpatterns = [
    path('', v.hora_extra_list, name='hora_extra_list'),
]


urlpatterns = [
    path('documento/', include(documento_urlpatterns)),
    path('funcionario/', include(funcionario_urlpatterns)),
    path('hora-extra/', include(hora_extra_urlpatterns)),
]
