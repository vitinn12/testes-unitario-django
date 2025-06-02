from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.index, name='index'),
    path('salvar/', views.salvar, name='salvar'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('editar_usuario/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('excluir_usuario/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
]
