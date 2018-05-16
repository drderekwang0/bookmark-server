from django.urls import path

from . import views

urlpatterns = [path("", views.get_bookmarks, name="get_bookmarks")]
