from django.urls import path, include

from game_play_app.web.views import index, dashboard, profile_create, profile_details, profile_edit, profile_delete, \
    game_create, game_details, game_edit, game_delete

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('game/', include([
        path('create/', game_create, name='game create'),
        path('details/<int:pk>/', game_details, name='game details'),
        path('edit/<int:pk>/', game_edit, name='game edit'),
        path('delete/<int:pk>/', game_delete, name='game delete'),
    ])),
)
