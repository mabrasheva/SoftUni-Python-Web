from django.urls import path

from fruitipedia_app.user_profile.views import profile_create, profile_details, profile_edit, profile_delete

urlpatterns = (
    path("create/", profile_create, name="profile_create"),
    path("details/", profile_details, name="profile_details"),
    path("edit/", profile_edit, name="profile_edit"),
    path("delete/", profile_delete, name="profile_delete"),
)
