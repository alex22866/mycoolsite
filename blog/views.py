from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from blog.models import *


def index(request):
    categories = Category.objects.all()
    cat_list = []
    print(cat_list)
    for c in categories:
        post = Post.objects.filter(category_id=c.id)
        if post:
            cat_list.append(c.id)
    cat = categories.filter(id__in=cat_list)
    authors = Author.objects.all()
    users = User.objects.all()
    try:
        category_fan = Category.objects.get(title='Фантастика')
    except ObjectDoesNotExist:
        raise ValueError('Такой категории не существует')

    params = {
        'categories': cat,
        'fan': category_fan,
        'authors': authors,
        'users': users,
    }
    return render(request, 'index.html', params)


def category(request, pk):
    posts = Post.objects.filter(category_id=pk)
    return render(request, 'category.html', locals())


def author(request, pk):
    posts = Post.objects.filter(author_id=pk)
    params = {
        'posts': posts
    }
    return render(request, 'posts_by_authors.html', params)


def comments(request, pk):
    _comments = Comments.objects.filter(user_id=pk)
    params = {
        'comments': _comments,
    }
    return render(request, 'comments.html', params)

