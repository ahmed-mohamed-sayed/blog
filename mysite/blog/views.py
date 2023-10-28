from django.shortcuts import get_object_or_404, render
from.models import Post
from django.http import Http404

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, published__year=year, published__month=month, published__day=day, slug=slug)
    return render(request, 'blog/post/detail.html', {'post': post})