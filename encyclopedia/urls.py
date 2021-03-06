from django.urls import path
from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.display_entry, name="display_entry"),
    path("wiki/<str:title>/edit",views.edit_entry, name="edit_entry"),
    path("searchresults",views.search_results, name="search_results"),
    path("randomentry",views.random_entry, name="random_entry"),
    path("create_entry", views.create_entry, name="create_entry"),
]
