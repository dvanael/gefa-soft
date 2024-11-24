from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path("", include("app.users.urls")),
]

if settings.DEBUG:
    urlpatterns += [path("admin/", admin.site.urls)]
