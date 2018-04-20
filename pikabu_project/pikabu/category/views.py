from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category

# Create your views here.
from django.views.generic import ListView


def category_page(request):

    return HttpResponse("Tags")

def category_posts_page(request, name_of_category):

    category = get_object_or_404(Category.objects.all(), title = name_of_category)

    return render(request, 'category/category_detail.html', {'category': category})

class CategoryList(ListView):

    template_name = "category/categoryes.html"
    model = Category
