from django.urls import path

from online_library.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
