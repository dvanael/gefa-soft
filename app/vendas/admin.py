from django.contrib import admin
from .models import Venda, ProdutoVenda
# Register your models here.

admin.site.register(ProdutoVenda)
class ProdutoVendaInline(admin.TabularInline):
    model = ProdutoVenda
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    inlines = [ProdutoVendaInline]


admin.site.register(Venda, VendaAdmin)