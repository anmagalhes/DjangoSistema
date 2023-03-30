from django.urls import include, path

from backend.estoque import views as v

app_name = 'estoque'


categoria_urlpatterns = [
    path('', v.categoria_list, name='categoria_list'),
    path('create/', v.CategoriaCreateView.as_view(), name='categoria_create'),
]

estoque_urlpatterns = [
    path('', v.estoque_list, name='estoque_list'),
    path('create/', v.EstoqueCreateView.as_view(), name='estoque_create'),
]

produto_urlpatterns = [
    path('', v.produto_list, name='produto_list'),
    path('create/', v.ProdutoCreateView.as_view(), name='produto_create'),
]


urlpatterns = [
    path('categoria/', include(categoria_urlpatterns)),
    path('estoque/', include(estoque_urlpatterns)),
    path('produto/', include(produto_urlpatterns)),
]
