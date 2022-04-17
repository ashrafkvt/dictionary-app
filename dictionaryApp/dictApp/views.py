from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import requests
from bs4 import BeautifulSoup

# Create your views here.


def home(request):
    if request.method ==  "POST":
        word = request.POST['word']
        print(word)
        word_url = 'https://www.dictionary.com/browse/'+word
        req = requests.get(word_url)
        response_content = req.content
        soup = BeautifulSoup(response_content, 'html.parser')
        span = soup.find_all("span", {"class":"one-click-content"})
        data = {}
        data['word'] = word
        if len(word) == 0:
            data['meaning'] = "Please enter a word to search"
        else:
            if len(span) > 0:
                data['meaning'] = span[0].text
            else:
                data['meaning'] = "please recheck what you've entered"
        return render(request, 'dictApp/home.html', data)
    else:
        print("sdbsjdbsd")
        return render(request, 'dictApp/home.html')