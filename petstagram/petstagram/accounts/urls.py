from django.urls import path, include

from petstagram.accounts.views import register_account, login_account, show_account_details, edit_account, \
    delete_account

urlpatterns = (
    path('register/', register_account, name='register account'),
    path('login/', login_account, name='login account'),
    path('profile/<int:pk>/', include([
        path('', show_account_details, name='show account details'),
        path('edit/', edit_account, name='edit account'),
        path('delete/', delete_account, name='delete account'),
    ]))
)
