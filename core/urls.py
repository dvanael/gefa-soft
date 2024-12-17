from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path("", include("app.users.urls")),
    path("produtos/", include("app.produtos.urls")),
    path("despesas/", include("app.despesas.urls")),
    path("funcionarios/", include("app.funcionarios.urls")),
    path("insumos/", include("app.insumos.urls")),
    path("vendas/", include("app.vendas.urls")),
]

if settings.DEBUG:
    urlpatterns += [path("admin/", admin.site.urls)]
