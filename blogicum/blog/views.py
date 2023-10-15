from datetime import datetime

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category

PUBLISH_POSTS = 5


def posts():
    posts = Post.objects.all().select_related(
        'author',
        'location',
        'category'
    )
    return posts


def index(request):
    return render(
        request,
        'blog/index.html',
        {'post_list': posts().filter(
                pub_date__lte=datetime.now(),
                is_published=True,
                category__is_published=True
        ).order_by('-pub_date')[:PUBLISH_POSTS]}
    )


def post_detail(request, post_id):
    return render(request,
                  'blog/detail.html',
                  {'post': get_object_or_404(
                      Post,
                      pk=post_id,
                      pub_date__lte=datetime.now(),
                      is_published=True,
                      category__is_published=True)}
                  )


def category_posts(request, category_slug):
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True
                                 )
    post_list = posts().filter(
        category=category,
        is_published=True,
        pub_date__lte=datetime.now()
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
