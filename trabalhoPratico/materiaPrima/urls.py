from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index1'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path("detalhe/<int:pk>/", views.detalhe, name='detalhe'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
]