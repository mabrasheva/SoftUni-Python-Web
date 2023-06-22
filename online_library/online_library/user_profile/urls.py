from django.urls import path

from online_library.user_profile.views import profile_details, profile_edit, profile_delete

urlpatterns = (
    path('', profile_details, name='profile details'),
    path('edit/', profile_edit, name='profile edit'),
    path('delete/', profile_delete, name='profile delete'),
)
