from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Post
from comments.models import Comment

# Create your views here.

def best_posts_list_page(request):

    #post_list = Post.objects.all()

    #return render(request, 'post/best.html', {'post_list': post_list})
    return HttpResponse("post_list")

def new_posts_list_page(request):

    return HttpResponse("new posts list")

def post_page(request, post_id):

    post = get_object_or_404(Post.objects.all(), id = post_id)

    return render(request, 'post/post_detail.html', {'post': post})
    #return HttpResponse(post_id)

class PostBestList(ListView):

    template_name = "post/best.html"
    model = Post


class PostNewList(ListView):

    template_name = "post/new.html"
    model = Post

class PostCreate(CreateView):

    template_name = 'post/create_post.html'
    model = Post
    fields = 'title', 'content_text', 'category'

    def get_success_url(self):

        return reverse('post:post_page', kwargs={'post_id': self.object.pk})

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

class PostUpdate(UpdateView):

    template_name = 'post/edit_post.html'
    model = Post
    fields = 'title', 'content_text'
    pk_url_kwarg = 'post_id'

    def get_queryset(self):
        return super(PostUpdate, self).get_queryset().filter(author=self.request.user)


    def get_success_url(self):
        return reverse('post:post_page', kwargs={'post_id': self.object.pk})

class CommentCreate(UpdateView):

    template_name = 'post/post_detail.html'
    model = Comment
    fields = 'content_text'

    def get_success_url(self):

        return reverse('post:post_page', kwargs={'post_id': self.object.pk})

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super(CommentCreate, self).form_valid(form)


