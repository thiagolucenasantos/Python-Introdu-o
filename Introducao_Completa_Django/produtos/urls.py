from django.urls import path # importando o path de urls do django
from . import views #importando o arquivo views da própria pasta produtos
urlpatterns = [
    path('cadastrar/', views.cadastrar), #funcão cadastrar criada no arquivo views.py
    path('listar/', views.listar),
    path('deletar/<int:id>/', views.deletar)
]