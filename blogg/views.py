from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
import requests
from django.conf import settings

def home(request):
    if request.method == "GET":
        data = fetch_news_data()
        return render(request, 'posts.html', {'data':data})
    

def fetch_news_data(page=1, page_size=20):
    api_key = settings.NEWS_API_KEY
    url = ('https://newsapi.org/v2/everything?domains=br.ign.com,gamespot.com,kotaku.com,polygon.com,metacritic.com,rockpapershotgun.com,gameinformer.com&sortBy=popularity&'f'apiKey={api_key}&page={page}&pageSize={page_size}')
    response = requests.get(url)
    data = response.json()
    return data
    
    
    
