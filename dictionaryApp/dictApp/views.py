from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import requests
from bs4 import BeautifulSoup

# Create your views here.


def home(request):
    return render(request, 'dictApp/home.html')