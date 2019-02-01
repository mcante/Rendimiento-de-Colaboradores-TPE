

from django.urls import path, include

from .views import CategoriaCreateView, CategoriaUpdateView, CategoriaListView, \
NotaCreateView, NotaUpdateView, NotaListView, NotaDetailView, NotaSeguimientoListView

urlpatterns = [
    # Categoria
    path('categorias/list/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/add/', CategoriaCreateView.as_view(), name='categoria_add'),
    path('categoria/update/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/detail/<int:pk>/', NotaDetailView.as_view(), name='categoria_detail_notas'),

    # Nota
    path('notas/list/', NotaListView.as_view(), name='nota_list'),
    path('notas/seguimiento/list/', NotaSeguimientoListView.as_view(), name='nota_seguimiento_list'),
    path('nota/add/', NotaCreateView.as_view(), name='nota_add'),
    path('nota/update/<int:pk>/', NotaUpdateView.as_view(), name='nota_update'),

]
