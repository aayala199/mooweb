from turtle import pos
from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog(request):
    posts=Post.objects.all()
    return render(request,"home/blog.html", {"posts": posts}) 
