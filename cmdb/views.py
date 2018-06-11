from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from cmdb import models
list = [{"username":"1","password":"1"},
        {"username":"2","password":"2"}]

def index(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        #print(username,password)
        #temp = {"username":username,"password":password}
        #list.append(temp)

        models.message.objects.create(username=username, password=password)
        #models.message.save()
        people_list = models.message.objects.all()
    return render(request,"index.html",{"data":people_list})