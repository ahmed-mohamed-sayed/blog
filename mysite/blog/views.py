from django.shortcuts import render
from.models import Post
from django.http import Http404

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'blog/post/detail.html', {'post': post})

# D:\blog\src\mysite\blog\templates\posts\list.html