from django.contrib import admin
from .models import Post, ContentSection, Comment

class ContentSectionInline(admin.StackedInline):
    model = ContentSection
    extra = 1
    fields = ('title', 'text_block', 'images_or_videos1', 'images_or_videos2', 'images_or_videos3', 'images_or_videos4', 'images_or_videos5') 
    max_num = 10

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'is_active', 'average_rating')
    list_filter = ('category', 'created_at', 'author')
    search_fields = ('title', 'caption')
    ordering = ('-created_at',)
    fields = ('title','image', 'caption', 'category', 'is_active',)
    readonly_fields = ('created_at',)
    list_editable = ("is_active",)
    inlines = [ContentSectionInline] 

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
admin.site.register(ContentSection)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'rating', 'created_at', 'is_active')
    list_filter = ('created_at', 'is_active', 'rating',)
    search_fields = ('content', 'author__username', 'post__title')