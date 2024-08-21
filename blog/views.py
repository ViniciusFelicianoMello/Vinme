from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg

from django.contrib.auth.decorators import user_passes_test

from .forms import CommentForm, ContentSectionForm, PostForm
from .models import ContentSection, Post, Comment

from vinme.views import pages, add_pages_context
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def superuser_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func

def blog(request):
    travel = [
        {'url': '#banner', 'icon': 'fa-solid fa-pager', 'text': 'Banner'},
        {'url': '#recents', 'icon': 'fa-solid fa-clock', 'text': 'Recentes'},
        {'url': '#popular', 'icon': 'fa-solid fa-star', 'text': 'Populares'},
    ]

    selected_categories = request.GET.get('categories', '')
    if selected_categories:
        selected_categories = selected_categories.split(',')
        posts = Post.objects.filter(category__in=selected_categories, is_active=True).annotate(
            calculated_average_rating=Avg('comments__rating')
        ).order_by('-created_at')
    else:
        posts = Post.objects.filter(is_active=True).annotate(
            calculated_average_rating=Avg('comments__rating')
        ).order_by('-created_at')

    popular_posts = Post.objects.filter(is_active=True).annotate(
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

@superuser_required
def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        section_forms = [ContentSectionForm(request.POST, request.FILES, prefix=f'section_{i}') for i in range(10)]

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()

            for form in section_forms:
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
        'form_title': 'Adicionar post',
        'button_text': 'Publicar',
        'image_status': 'Nenhuma imagem selecionada'
    }

    context = add_pages_context(context)

    return render(request, 'blog/post_form.html', context)


@superuser_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        # Carregar seções existentes e adicionar novas seções se necessário
        sections = list(post.sections.all()) + [ContentSection(post=post) for _ in range(10 - post.sections.count())]
        section_forms = [ContentSectionForm(request.POST, request.FILES, instance=section, prefix=f'section_{i}') for i, section in enumerate(sections)]

        if post_form.is_valid():
            post_form.save()
            for form in section_forms:
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
        post_form = PostForm(instance=post)
        # Criar formulários para as seções existentes e adicionar novos se necessário
        sections = list(post.sections.all()) + [ContentSection(post=post) for _ in range(10 - post.sections.count())]
        section_forms = [ContentSectionForm(instance=section, prefix=f'section_{i}') for i, section in enumerate(sections)]

    context = {
        'post_form': post_form,
        'section_forms': section_forms,
        'image_indices': range(5),
        'numbers': range(1, 11),
        'form_title': 'Editar post',
        'button_text': 'Atualizar',
        'image_status': 'Imagem selecionada' if post.image else 'Nenhuma imagem selecionada'
    }

    context = add_pages_context(context)

    return render(request, 'blog/post_form.html', context)

@superuser_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    return redirect('blog') 

@superuser_required
def deactivate_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST' and request.user == post.author:
        post.is_active = False
        post.save()
    
    return redirect('blog')


def post_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_page', post_id=post.id)
    else:
        form = CommentForm()
    
    comments = post.comments.filter(is_active=True).order_by('-created_at')
    
    context = {
        'post': post,
        'form': form,
        'comments': comments,
    }
    context = add_pages_context(context)
    return render(request, 'blog/post_page.html', context)

#comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user != comment.author:
        return HttpResponseForbidden("Você não tem permissão para excluir este comentário.")
    
    if request.method == 'POST':
        post_id = comment.post.id
        comment.delete()
        return redirect('post_page', post_id=post_id)
    
    return HttpResponseForbidden("Método não permitido.")