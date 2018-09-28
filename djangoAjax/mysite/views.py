from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json

# Create your views here.

def index(request):
    return render(request,"index.html")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def ajax_list(request):
    return JsonResponse(range(100),safe=False)

def ajax_dict(request):
    dic={"key":"123","values":"value"}
    return JsonResponse(dic)