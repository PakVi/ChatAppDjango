from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework import permissions
from chat.models import *
from chat.serializers import *

# class AddRoomView(CreateView):
#     model = Room
#     form_class = RoomForm
#     template_name = 'add_room.html'

# def addRoomView(request):
#     form = RoomForm()
#     Room.objects.create(
#
#         name=request.POST.get('name'),
#     )
#     return redirect('rooms')
#     # template_name = 'add_room.html'
#     context = {'form': form}
#     return render(request, 'room/add_room.html', context)
#




class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


def index_view(request):
    return render(request, 'chat/index.html', {
        'rooms': Room.objects.all(),
    })






# @login_required
# def rooms(request):
#     rooms = Room.objects.all()
#
#     return render(request, 'room/rooms.html', {'rooms': rooms})
#
# @login_required
# def room(request, slug):
#     room = Room.objects.get(slug=slug)
#     messages = Message.objects.filter(room=room)[0:25]
#
#     return render(request, 'room/

@login_required
def room_view(request, room_name):
    try:
        chat_room = Room.objects.get(name=room_name)
    except ObjectDoesNotExist:
        chat_room, created = Room.objects.get_or_create(name=room_name, owner=request.user)
    return render(request, 'chat/room.html', {
        'room': chat_room,
    })

