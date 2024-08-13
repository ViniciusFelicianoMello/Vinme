from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg

from django.contrib.auth.decorators import user_passes_test

from .forms import CommentForm, ContentSectionForm, PostForm
from .models import Post

from vinme.views import pages, add_pages_context

def superuser_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func

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

    context = {
        'form': form,
    }
    context = add_pages_context(context) 
    return render(request, 'post_detail.html', context)



@superuser_required
def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        content_section_form = ContentSectionForm(request.POST, request.FILES)
        if post_form.is_valid() and content_section_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            
            content_section = content_section_form.save(commit=False)
            content_section.post = post
            content_section.save()
            
            return redirect('blog')
    else:
        post_form = PostForm()
        content_section_form = ContentSectionForm()
    
    context = {
        'post_form': post_form,
        'content_section_form': content_section_form,
    }
    context = add_pages_context(context) 
    return render(request, 'blog/post_form.html', context)

@superuser_required
def edit_post(request, post_id):

    context = add_pages_context(context) 
    return render(request, 'blog/post_form.html', context)