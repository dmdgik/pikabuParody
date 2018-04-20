from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from post.views import *

urlpatterns = [
    url(r'^best/$', PostBestList.as_view(), name="post_best_list"),
    url(r'^new/$', PostNewList.as_view(), name="post_new_list"),
    url(r'^post/(?P<post_id>\d+)/$', post_page, name="post_page"),
    url(r'^post_create/$', login_required(PostCreate.as_view()), name="post_create"),
    url(r'^post/(?P<post_id>\d+)/edit/$', login_required(PostUpdate.as_view()), name="post_edit"),
]