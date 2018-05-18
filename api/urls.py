from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_bookmarks, name="get_bookmarks"),
    path("batch_add", views.batch_add, name="batch_add"),
    path("<int:id>/actions/read", views.read_bookmark, name="read"),
    path("<int:id>/actions/delete", views.delete_bookmark, name="delete"),
]
