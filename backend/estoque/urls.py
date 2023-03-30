from django.urls import include, path

from backend.estoque import views as v

app_name = 'estoque'


categoria_urlpatterns = [
    path('', v.categoria_list, name='categoria_list'),
]

estoque_urlpatterns = [
    path('', v.estoque_list, name='estoque_list'),
]

produto_urlpatterns = [
    path('', v.produto_list, name='produto_list'),
]


urlpatterns = [
    path('categoria/', include(categoria_urlpatterns)),
    path('estoque/', include(estoque_urlpatterns)),
    path('produto/', include(produto_urlpatterns)),
]
