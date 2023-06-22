from django.urls import path
from online_library.book.views import book_add, book_edit, book_details, book_delete

urlpatterns = (
    path('add/', book_add, name='book add'),
    path('edit/<int:pk>/', book_edit, name='book edit'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('delete/<int:pk>/', book_delete, name='book delete'),
)
