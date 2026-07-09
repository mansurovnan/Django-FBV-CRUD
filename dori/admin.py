from django.contrib import admin
from .models import Drug


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "fabric",
        "price",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "id",
        "name",
    )

    list_filter = (
        "is_active",
        "fabric",
    )

    search_fields = (
        "name",
        "desc",
        "fabric",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 10