from django.urls import path
from .views import (
    user_list,
    create_user,
    detail_user,
    delete_user,
)

urlpatterns = [
    path("list/", user_list, name="user_list"),
    path("create/", create_user, name="create_user"),
    path("detail/<int:id>/", detail_user, name="detail_user"),
    path("delete/<int:id>/", delete_user, name="delete_user"),
]