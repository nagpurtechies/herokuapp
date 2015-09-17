from django.http import HttpResponse
from .models import Post
from django.template import RequestContext, loader
# Create your views here.


def index(request):
    latest_posts = Post.objects.order_by("-pub_date")
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_posts_list': latest_posts,
    })
    latest_posts = ', '.join([p.title for p in latest_posts])
    return HttpResponse(template.render(context))
