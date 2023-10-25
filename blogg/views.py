from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
import requests
from django.conf import settings
from slugify import slugify


def home(request):
    if request.method == "GET":
        data = fetch_news_data(request)
        articles, page_number, page_size = data
        if 'articles' in articles:
            add_slugs_data(articles['articles'])
            total_results = articles['totalResults']
            total_pages = total_results // page_size
        
        
        return render(request, 'posts.html', {'page':articles['articles'], 'page_number':page_number, 'page_size':page_size, 'total_pages':total_pages})
    

def fetch_news_data(request):
    page = request.GET.get('page', 1)
    page_size = 100
    
    api_key = settings.NEWS_API_KEY
    url = ('https://newsapi.org/v2/everything?domains=br.ign.com,gamespot.com,kotaku.com,polygon.com,metacritic.com,rockpapershotgun.com,gameinformer.com&sortBy=popularity&'f'apiKey={api_key}&page={page}&pageSize={page_size}')
    response = requests.get(url)
    data = response.json()
    return (data, int(page), page_size)


def generate_unique_slug(new_slug, count=0):
    final_slug = new_slug
    if count > 0:
        final_slug = f'{new_slug}-{count}'
        
    if Post.objects.filter(slug=final_slug).exists():
        count += 1
        return generate_unique_slug(new_slug, count)
    return final_slug

def add_slugs_data(articles):
    for article in articles:
        article['slug'] = slugify(article['title'])
        slug = generate_unique_slug(article['slug'])
        author_name = article['author']
        user, created = User.objects.get_or_create(username=author_name)
        if created:
            user.first_name = author_name
            user.save()
            
        
        post, created = Post.objects.get_or_create(
            titulo = article['title'],
            slug = slug,
            autor = user,
            data = article['publishedAt']
        )
        if not created:
            post.slug = article['slug']
            post.save()

def post_content(request, id_post):
    pass
    
    
