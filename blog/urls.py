from django.urls import path

from . import views

# app_name = "blog"  # Learn how to use namespaces

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("category/<category>", views.blog_category, name="blog_category"),
    path("post/<int:pk>", views.blog_detail, name="blog_detail"),
]
