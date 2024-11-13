from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]
# django.contrib.auth.urls will provide access to the default login and logout views
