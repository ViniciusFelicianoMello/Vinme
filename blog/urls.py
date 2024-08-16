from django.urls import path
from blog.views import blog, create_post, edit_post, post_page

urlpatterns = [
    path('', blog, name='blog'),
    path('post/new/', create_post, name='create_post'),
    path('post/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('post/<int:post_id>/page/', post_page, name='post_page'),
    ] 
