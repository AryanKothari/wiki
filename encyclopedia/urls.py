from django.urls import path
from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.display_entry, name="display_entry"),
    path("wiki/<str:title>/edit",views.edit_page, name="edit_page"),
    path("create_page", views.create_page, name="create_page"),
]
