from django.http import HttpResponse
from .models import Post
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
# Create your views here.


def index(request):
    latest_posts = Post.objects.order_by("-pub_date")
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_posts_list': latest_posts,
    })
    latest_posts = ', '.join([p.title for p in latest_posts])
    return HttpResponse(template.render(context))


def post_detail(request, post_id):
    # post = get_object_or_404(Post, pk=post_id)
    return HttpResponse("Hello {}".format(post_id))
    # return render(request, 'details.html', {'post': post})
