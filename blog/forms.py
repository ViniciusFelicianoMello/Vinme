from django import forms
from .models import ContentSection, Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'rating']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'account_input'}),
            'rating': forms.RadioSelect(attrs={'class': 'rating_comment'}),
        }

class ContentSectionForm(forms.ModelForm):
    class Meta:
        model = ContentSection
        fields = ['title', 'text_block', 'images_or_videos1', 'images_or_videos2', 'images_or_videos3', 'images_or_videos4', 'images_or_videos5']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'account_input'}),
            'text_block': forms.Textarea(attrs={'class': 'account_input'}),
            'images_or_videos1': forms.ClearableFileInput(attrs={'class': 'account_input', 'style': 'display: none;'}),
            'images_or_videos2': forms.ClearableFileInput(attrs={'class': 'account_input', 'style': 'display: none;'}),
            'images_or_videos3': forms.ClearableFileInput(attrs={'class': 'account_input', 'style': 'display: none;'}),
            'images_or_videos4': forms.ClearableFileInput(attrs={'class': 'account_input', 'style': 'display: none;'}),
            'images_or_videos5': forms.ClearableFileInput(attrs={'class': 'account_input', 'style': 'display: none;'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'category', 'caption']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'account_input', 'style': 'display: none;'}),
            'title': forms.TextInput(attrs={'class': 'account_input'}),
            'caption': forms.Textarea(attrs={'class': 'account_input'}),
            'category': forms.Select(attrs={'class': 'account_input'}),
        }