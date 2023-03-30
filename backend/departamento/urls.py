from django.urls import include, path

from backend.departamento import views as v

app_name = 'departamento'


departamento_urlpatterns = [
    path('', v.departamento_list, name='departamento_list'),
]


urlpatterns = [
    path('', include(departamento_urlpatterns)),
]
