from django.urls import path
from .views import (
    home,
    drug_list,
    create_drug,
    detail_drug,
    delete_drug,
)

urlpatterns = [
    path("", home, name="home"),
    path("list/", drug_list, name="drug_list"),
    path("create/", create_drug, name="create_drug"),
    path("detail/<int:id>/", detail_drug, name="detail_drug"),
    path("delete/<int:id>/", delete_drug, name="delete_drug"),
]