from django.urls import path
from .views import UserListView, VirtualsListCreate, VitualsRetrieveUpdateDestroy
from . import views

urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
    path('virtuals/', VirtualsListCreate.as_view(), name='item-list'),
    path('virtuals/<uuid:pk>/', VitualsRetrieveUpdateDestroy.as_view(), name='item-detail'),
]