from django.urls import path
from blog import views
from blog.views import blog, create_post, edit_post, post_page, delete_post, delete_comment

urlpatterns = [
    path('', blog, name='blog'),
    path('post/new/', create_post, name='create_post'),
    path('post/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('post/<int:post_id>/page/', post_page, name='post_page'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('post/<int:post_id>/deactivate/', views.deactivate_post, name='deactivate_post'),
    path('comment/<int:comment_id>/delete', delete_comment, name='delete_comment'),
]