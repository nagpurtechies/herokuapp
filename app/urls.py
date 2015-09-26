from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail, name='details'),
    url(r'^create$', views.create, name='create')
]
