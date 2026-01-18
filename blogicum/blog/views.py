# from django.http import Http404
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .models import Post, Category

# Create your views here.


def get_published_posts():
    return Post.objects.select_related(
        "author",
        "location",
        "category"
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    template_name = "blog/index.html"
    post_list = get_published_posts()[:5]
    context = {
        "post_list": post_list,
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = "blog/detail.html"

    post = get_object_or_404(
        Post,
        pk=post_id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )

    context = {
        "post": post,
    }

    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.select_related(
        'author', 'location', 'category').filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category=category
    )

    context = {'category': category, 'post_list': post_list}
    return render(request, template_name, context)
