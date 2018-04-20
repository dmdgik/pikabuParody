from django.conf.urls import url
from category.views import *

urlpatterns = [
    url(r'^category/$', CategoryList.as_view(), name="categories_list"),
    url(r'^category/(?P<name_of_category>\w+)/$', category_posts_page, name="category_posts"),
]