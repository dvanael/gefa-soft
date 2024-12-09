from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path("", include("app.users.urls")),
    # path("", include("app.produtos.urls")),
    path("despesas/", include("app.despesas.urls")),
    path("", include("app.funcionarios.urls")),
    path("", include("app.insumos.urls")),
]

if settings.DEBUG:
    urlpatterns += [path("admin/", admin.site.urls)]
