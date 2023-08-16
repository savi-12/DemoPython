from django.http import HttpResponse
from django.shortcuts import render
from . models import place


#
def demo(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})
# def demo(request):
#     obj1=people.objects.all()
#     return render(request,"index.html",{'results':obj1})
# def result(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#     return render(request,"result.html",{'Result1':res1,'Result2':res2,'Result3':res3,'Result4':res4})

