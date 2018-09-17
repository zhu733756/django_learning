from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("欢迎光临，mysite！")

def add(request,a,b):
    href='%s/%s'%(a,b)
    return render(request,"add.html")

def home(request):
    string="zhuhan"
    empty_list=[]
    learn_list=["HTML","CSS","jQuery","Python","Django"]
    dict_info={"site":"mysite","content":"各种装逼技术"}
    return render(request,'home.html',{"string":string,
                                       'empty_list':empty_list,
                                       "learn_list":learn_list,
                                       "dict_info":dict_info})