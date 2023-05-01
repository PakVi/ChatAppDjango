from django.urls import path
# from .views import AddRoomView
from chat.views import *
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', index_view, name='chat-index'),
    # path('add_room/', AddRoomView.as_view(), name="add-room"),
    path('<str:room_name>/', room_view, name='chat-room'),
]
