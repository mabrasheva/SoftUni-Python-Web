from django.urls import path, include

from fruitipedia_app.fruit.views import fruit_create, fruit_details, fruit_edit, fruit_delete

urlpatterns = (
    path("create/", fruit_create, name="fruit_create"),
    path("<int:pk>/", include([
        path("details/", fruit_details, name="fruit_details"),
        path("edit/", fruit_edit, name="fruit_edit"),
        path("delete/", fruit_delete, name="fruit_delete"),
    ]), ),
)
