from django.shortcuts import render
from .models import Category, Post, Comment

# Create your views here.
def indexView(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts,}
    return render(request, 'blogs/index.html', context)

def blogDetail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        }
    return render(request, 'blogs/detail.html', context)

def blogCategory(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, 'blog/category.html', context)