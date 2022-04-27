from django.shortcuts import render

rooms = [
    {"id":1, "name": "Room 1"},
    {"id":2, "name": "Room 2"},
    {"id":3, "name": "Room 3"},
    {"id":4, "name": "Room 4"},
    
]

# Create your views here.
def home(request):
    context = {"rooms":rooms}
    return render(request, "home.html",context)

def room(request,pk):
    room = None
    for i in rooms:
        if(i['id'] == int(pk)):
            room = i
    context = {"room":room}
    return render(request, "room.html", context)