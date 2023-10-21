from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def home(request):
    posts = Post.objects.all()
    if request.method == "GET":
        return render(request, 'posts.html', {'posts':posts})
    
def post(request, slug):
    post = Post.objects.filter(slug=slug)
    if request.method == "GET":
        return render(request, 'conteudo.html', {'posts': post})