from django.shortcuts import render
import json
import requests

# Create your views here.
from another.models import AnotherModel


def data(request):
    response = requests.get("http://127.0.0.1:8000/api/info/")
    data = json.loads(response.text)
    context = {
        'data': data
    }
    return render(request, 'data/data.html', context)


def info(request):

