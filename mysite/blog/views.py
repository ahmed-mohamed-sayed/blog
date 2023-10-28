from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, render
from.models import Post
from django.http import Http404
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger

    # Create your views here.
    # def post_list(request):
    #     post_list = Post.objects.all()
    #     paginator = Paginator(post_list, 3)
    #     page_number = request.GET.get('page',1)
    #     posts = paginator.get_page(page_number)
    #     return render(request, 'blog/post/list.html', {'posts': posts})

class PostListView(ListView):
    ''' alternative way to create a list view '''
    model = Post
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'
        

# Create your views here.
def post_detail(request, year, month, day, slug):
    try:
        post = Post.objects.get(published__year=year, published__month=month, published__day=day, slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    # Check if the post is published or if the user is a superuser (admin).
    if post.status == Post.Status.PUBLISHED or request.user.is_superuser:
        return render(request, 'blog/post/detail.html', {'post': post})
    else:
        raise Http404("Post does not exist")


