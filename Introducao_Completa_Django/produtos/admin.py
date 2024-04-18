from django.contrib import admin
from .models import Produto #importando tabela produto para o banco de dados

# Register your models here.

admin.site.register(Produto) #registrando no banco


