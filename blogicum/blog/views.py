from django.shortcuts import render
from django.http import Http404


def index(request):
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, post_id: int):
    if post_id > len(posts) - 1:
        raise Http404
    return render(request, 'blog/detail.html', {'post': POSTS_DICT[post_id]})


def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {'category': category_slug})
