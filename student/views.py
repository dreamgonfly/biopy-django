from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student_view(request):
    return HttpResponse('hello world')

from json import dumps
def json(request, msg):
    obj = {'hi': msg}
    j = dumps(obj)
    return HttpResponse(j)
