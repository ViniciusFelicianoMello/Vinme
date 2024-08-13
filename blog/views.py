from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg

from blog import models
from .forms import CommentForm
from django import forms
from .models import Post, Comment
# from .forms import CommentForm

from vinme.views import pages, add_pages_context

def blog(request):
    travel = [
        {'url': '#banner', 'icon': 'fa-solid fa-pager', 'text': 'Banner'},
        {'url': '#popular', 'icon': 'fa-solid fa-star', 'text': 'Populares'},
        {'url': '#recents', 'icon': 'fa-solid fa-clock', 'text': 'Recentes'},
    ]

    selected_categories = request.GET.get('categories', '')
    if selected_categories:
        selected_categories = selected_categories.split(',')
        posts = Post.objects.filter(category__in=selected_categories).annotate(
            calculated_average_rating=Avg('comments__rating')
        ).order_by('-created_at')
    else:
        posts = Post.objects.annotate(
            calculated_average_rating=Avg('comments__rating')
        ).order_by('-created_at')

    popular_posts = Post.objects.annotate(
        calculated_average_rating=Avg('comments__rating')
    ).order_by('-calculated_average_rating')[:4]

    context = {
        'travel': travel,
        'posts': posts,
        'popular_posts': popular_posts,
        'selected_categories': selected_categories,
        'all_categories': Post.CATEGORIES,
    }
    
    context = add_pages_context(context) 

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'blog/partials/_post_list.html', context)
    else:
        return render(request, 'blog/blog.html', context)
    


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(post.get_absolute_url())
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'form': form})