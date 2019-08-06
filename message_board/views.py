from django.shortcuts import render

from .models import Message

# Create your views here.
def index(request):
    msg_list = Message.objects.all()
    for i in range(len(msg_list)):
        msg = msg_list[i]
        msg.date_time = msg.date_time.strftime('%Y-%m-%d %H:%M:%S')
        msg.index = i + 1
    context = {'msg_list': msg_list}
    
    return render(request, 'message/index.html', context)

def msg_create(request):
    content = request.POST.get('content', default=None)
    if content:
        msg = Message(content=content)
        msg.save()
    
    return index(request)