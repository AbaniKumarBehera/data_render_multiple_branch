from django.shortcuts import render

def data_render(request):
    d={'name':'ROHAN','age':'70'}
    return render(request,'data_render.html',context=d)

def jinja_operations(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'jinja_operations.html',context=d)
