from django.shortcuts import render

def data_render(request):
    d={'name':'ROHAN','age':'70'}
    return render(request,'data_render.html',context=d)