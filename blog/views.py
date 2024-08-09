from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Comment
# from .forms import CommentForm

from vinme.views import pages, add_pages_context

def blog(request):
    travel = [
        {'url': '#banner', 'icon': 'fa-solid fa-pager', 'text': 'Banner'},
        {'url': '#popular', 'icon': 'fa-solid fa-star', 'text': 'Populares'},
        {'url': '#latest', 'icon': 'fa-solid fa-clock', 'text': 'Recentes'},
    ]
    context = {'travel': travel}
    context = add_pages_context(context) 
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


from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),
        }