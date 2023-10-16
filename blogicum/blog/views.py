from datetime import datetime

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category

PUBLISH_POSTS = 5


def get_posts_qs():
    return Post.objects.all().select_related(
        'author',
        'location',
        'category'
    ).filter(
        pub_date__lte=datetime.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')


def index(request):
    return render(request,
                  'blog/index.html',
                  {'post_list': get_posts_qs()[:PUBLISH_POSTS]}
                  )


def post_detail(request, post_id):
    return render(request,
                  'blog/detail.html',
                  {'post': get_object_or_404(get_posts_qs(), pk=post_id)}
                  )


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_posts_qs().filter(category__slug=category_slug)
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
