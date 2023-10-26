from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.conf import settings
from slugify import slugify
from newsapi import NewsApiClient

def home(request):
    if request.method == "GET":
        data = fetch_news_data(request)
        articles, page_number, page_size = data
        if 'articles' in articles:
            add_slugs_data(articles['articles'])
            
        print(articles)
        return render(request, 'posts.html', {'page':articles['articles'], 'page_number':page_number, 'page_size':page_size})
         

def fetch_news_data(request, page_number=1, page_size=100):
    current_page = request.GET.get('page', page_number)
    
    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
    
    all_articles = []
    
    for i in range(page_number, page_number + 3):
        response = newsapi.get_everything(
            domains='br.ign.com,gamespot.com,kotaku.com,polygon.com,metacritic.com,rockpapershotgun.com,gameinformer.com',
            sort_by='popularity',
            page_size=page_size,
            page=i
        )
        articles = response['articles']
        all_articles.extend(articles)
    
    return all_articles, int(current_page), page_size


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
    
    
