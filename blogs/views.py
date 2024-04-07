from django.shortcuts import render
from .models import Category, Post, Comment

# Create your views here.
def indexView(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}
    return render(request, 'blogs/index.html', context)