from django.urls import path
from .views import \
  redirect_to_homepage, display_homepage, \
  display_posts, display_tags, \
  create_post, create_tag, \
  display_post_details, display_associated_posts, \
  display_found_posts


urlpatterns = [
  path('', redirect_to_homepage, name='redirect_to_homepage'),
  path('home/', display_homepage, name='display_homepage'),

  path('home/posts/', display_posts, name='display_posts'),
  path('home/posts/create/', create_post, name='create_post'),
  path('home/posts/<str:slug>/', display_post_details, name='display_post_details'),

  path('home/tags/', display_tags, name='display_tags'),
  path('home/tags/create/', create_tag, name='create_tag'),
  path('home/posts/search/<str:search_query>', display_found_posts, name='display_found_posts'),
  path('home/tags/<str:slug>', display_associated_posts, name='display_associated_posts'),

]