from django.contrib import admin
from django.urls import path, include
from dori.views import home

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home Page
    path("", home, name="home"),

    # Drug App
    path("dori/", include("dori.urls")),

    # User App
    path("user/", include("user.urls")),
]