from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "email",
        "phone",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "id",
        "full_name",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 10