from django import forms
from .models import ContentSection, Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),
        }

class ContentSectionForm(forms.ModelForm):
    class Meta:
        model = ContentSection
        fields = ['title', 'text_block', 'images_or_videos']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'caption', 'category']