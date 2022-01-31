from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .consumers import ContactsLister
import json

def index(request):
    cl = ContactsLister()
    all_users = cl.get_all_users()
    return render(request, 'chat/index.html', {'all_users' : all_users , 'this_user':request.user})

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })