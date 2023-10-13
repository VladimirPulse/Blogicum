from django.shortcuts import render, get_object_or_404, get_list_or_404
from datetime import datetime
from blog.models import Post, Category


posts = Post.objects.all().select_related(
    'author',
    'location',
    'category'
).filter(
    pub_date__lte=datetime.now(),
    is_published=True,
    category__is_published=True
).order_by(
    '-pub_date'
)


def index(request):
    return render(request,
                  'blog/index.html',
                  {'post_list': posts[:5]}
                  )


def post_detail(request, post_id):
    return render(request,
                  'blog/detail.html',
                  {'post': get_object_or_404(posts, pk=post_id)}
                  )


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    post_list = get_list_or_404(posts, category_id=category.pk)
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
