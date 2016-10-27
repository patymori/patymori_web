from django.conf.urls import include, url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
]
