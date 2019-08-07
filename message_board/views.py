from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

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

def msg(request):
    msg_list = Message.objects.all()
    items = []
    for i in range(len(msg_list)):
        msg = msg_list[i]
        msg.index = i + 1
        msg.date_time = msg.date_time.strftime('%Y-%m-%d %H:%M:%S')
        item = {
            'pk': msg.index,
            'content': msg.content,
            'date_time': msg.date_time
        }
        items.append(item)
    
    return JsonResponse({'items': items}, safe=False)

def msg_create(request):
    content = request.POST.get('content', default=None)
    if content:
        msg = Message(content=content)
        msg.save()
    
    return index(request)