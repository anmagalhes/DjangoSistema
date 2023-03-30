from django.urls import include, path

from backend.pedido import views as v

app_name = 'pedido'


pedido_urlpatterns = [
    path('', v.pedido_list, name='pedido_list'),
    path('create/', v.PedidoCreateView.as_view(), name='pedido_create'),
    path('<int:pk>/update/', v.PedidoUpdateView.as_view(), name='pedido_update'),
]


urlpatterns = [
    path('', include(pedido_urlpatterns)),
]
