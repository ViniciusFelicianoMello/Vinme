from django.contrib import admin
from django.forms import ValidationError
from .models import Post, ContentSection, Media, Comment, Like

class MediaInline(admin.TabularInline):
    model = Media
    extra = 1
    fields = ('file', 'media_type')
    max_num = 5

class ContentSectionInline(admin.StackedInline):
    model = ContentSection
    extra = 1
    fields = ('title', 'text_block')
    inlines = [MediaInline]

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_active', 'average_rating')
    list_filter = ('category', 'created_at', 'author')
    search_fields = ('title', 'caption')
    ordering = ('created_at',)
    fields = ('title','image', 'caption', 'category', 'is_active',)
    inlines = [ContentSectionInline] 

admin.site.register(Post, PostAdmin)
admin.site.register(ContentSection)
admin.site.register(Media)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'rating', 'created_at', 'is_active')
    list_filter = ('created_at', 'is_active', 'rating',)
    search_fields = ('content', 'author__username', 'post', 'title')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')