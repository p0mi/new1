from django.urls import path
from .views import UserListView
from . import views

urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
]