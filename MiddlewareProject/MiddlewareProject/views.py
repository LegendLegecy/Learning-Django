from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from .main import GetCryptoDetails
from django.http import JsonResponse
import json
from .main import *


def index(request):
    return render(request , 'index.html' )



def loading(request):
    return render(request, 'loading.html')

def run_scraper(request):
    try:
        status=GetCryptoDetails()  # Your function that scrapes and saves data
        return JsonResponse({'status': status})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


def result(request):
    data=None
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return render(request, 'result.html', {'data': data})