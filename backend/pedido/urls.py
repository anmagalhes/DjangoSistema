from django.urls import include, path

from backend.pedido import views as v

app_name = 'pedido'


pedido_urlpatterns = [
    path('', v.pedido_list, name='pedido_list'),
]


urlpatterns = [
    path('', include(pedido_urlpatterns)),
]
