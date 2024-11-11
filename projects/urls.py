from django.urls import path
from . import views

# app_name = "pages"

urlpatterns = [
    path(
        "", views.projects_index, name="projects_index"
    ),  # path("", views.index, name="index"),
    path("<int:pk>", views.projects_detail, name="projects_detail"),
]
