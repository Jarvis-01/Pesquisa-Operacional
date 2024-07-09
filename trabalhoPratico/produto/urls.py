from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index2'),
    path('adiciona/', views.adicionar, name='adiciona'),
    path("detalhes/<int:produto_id>/", views.detalhes, name='detalhes'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
]
