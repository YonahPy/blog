from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.conf import settings
from slugify import slugify
from newsapi import NewsApiClient

def home(request):
    if request.method == "GET":
        data = fetch_news_data_page(request)
        articles, page_number= data
        
        if 'articles' in articles:
            add_slugs_data(articles['articles'])
            
            
        return render(request, 'posts.html', {'page':articles['articles'], 'page_number':page_number})
         

def fetch_news_data_page(request):
    current_page = request.GET.get('page', 1)
    
    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
    
    response = newsapi.get_everything(
        domains='br.ign.com,gamespot.com,kotaku.com,metacritic.com,rockpapershotgun.com,polygon.com,gameinformer.com',
        sort_by='popularity',
        page_size=20,
        page=int(current_page)
    )
    print(f'ola o numero da pagina é {current_page}')
    
    return response, current_page


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
    
    
