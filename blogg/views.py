from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    if request.method == "GET":
        return render(request, 'posts.html', {'posts':posts})
    
