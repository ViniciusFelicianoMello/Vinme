from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg

from django.contrib.auth.decorators import user_passes_test

from .forms import CommentForm, ContentSectionForm, PostForm
from .models import ContentSection, Post

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

def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        section_forms = [ContentSectionForm(request.POST, request.FILES, prefix=f'section_{i}') for i in range(10)]

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()

            # Itera sobre os formulários de seção
            for form in section_forms:
                # Verifica se o formulário é válido e se contém dados significativos
                if form.is_valid() and (
                    form.cleaned_data.get('title') or
                    form.cleaned_data.get('text_block') or
                    any(form.cleaned_data.get(f'images_or_videos{i}') for i in range(1, 6))
                ):
                    section = form.save(commit=False)
                    section.post = post
                    section.save()

            return redirect('blog')
    else:
        post_form = PostForm()
        section_forms = [ContentSectionForm(prefix=f'section_{i}') for i in range(10)]

    context = {
        'post_form': post_form,
        'section_forms': section_forms,
        'image_indices': range(5),
        'numbers': range(1, 11),
    }

    context = add_pages_context(context)

    return render(request, 'blog/post_form.html', context)


@superuser_required
def edit_post(request, post_id):

    context = add_pages_context(context) 
    return render(request, 'blog/post_form.html', context)