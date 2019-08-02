from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache

from .models import Information

import json

# Create your views here.
def info(request):
    info_list = Information.objects.all()
    items = []
    for i in range(len(info_list)):
        info = info_list[i]
        info.index = len(info_list) - i
        info.date_time = info.date_time.strftime('%Y-%m-%d %H:%M:%S')
        item = {
            'pk': info.index,
            'name': info.name,
            'phone': info.phone,
            'address': info.address,
            'date_time': info.date_time
        }
        items.append(item)
    
    return JsonResponse({'items': items}, safe=False)

@csrf_exempt
@never_cache
def info_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        info = Information(
            name = name,
            phone = phone,
            address = address
        )
        info.save()
        
        return JsonResponse({'result': 'ok'}, safe=False)
    else:
        return JsonResponse({'result': 'failed'}, safe=False)
