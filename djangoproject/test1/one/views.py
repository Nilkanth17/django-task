from django.shortcuts import render
from .models import Online
from .forms import Onlineform
from http import Res


# Create your views here.

def one_file(request):
    data = request.data
    name = data.get('name')
    description = data.get('description')

    name = request.POST['name']

    Online.objects.create(name=name,description=description)
    return Response()
    

