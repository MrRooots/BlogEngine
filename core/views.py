from django.shortcuts import render, redirect
from django.urls import resolve, Resolver404
from .models import Post, Tag
from .forms import PostCreationForm, TagCreationForm


# Function to create navigation bar
def get_path(request):
  urls = [i for i in request.path.split('/') if i != '']
  path = [i.title() for i in urls if i != '']
  links = []
  temp_path = '/'

  for url_part in urls:
    temp_path += url_part + '/'

    try:
      links.append(resolve(temp_path).view_name)
    except Resolver404:
      pass

  return zip(path, links)


# Simple redirect to homepage
def redirect_to_homepage(request):
  return redirect('home/')


# Function to render homepage template
def display_homepage(request):
  context = {
    'path': get_path(request),
    'search_placeholder': 'Search for posts',
  }
  return render(request, 'core/homepage.html', context=context)


# Function to render list of posts
def display_posts(request):
  context = {
    'posts': Post.objects.all(),
    'path': get_path(request),
    'search_placeholder': 'Search for posts'
  }
  return render(request, 'core/display_posts.html', context=context)


def create_post(request):
  if request.method == 'GET':
    context = {
      'form': PostCreationForm,
      'tags': enumerate(Tag.objects.all()),
      'path': get_path(request),
      'search_placeholder': 'Search for posts',
    }
    return render(request, 'core/post_creation_form.html', context=context)

  if request.method == 'POST':
    form = PostCreationForm(request.POST)

    if form.is_valid():
      for i in form.cleaned_data.values():
        print(i)

      form.save()
      return redirect('display_posts')

    else:
      context = {
        'form': PostCreationForm,
        'path': get_path(request),
        'search_placeholder': 'Search for posts',
      }
      return render(request, 'core/post_creation_form.html', context=context)


def display_post_details(request, slug):
  context = {
    'post': Post.objects.get(slug__iexact=slug),
    'path': get_path(request),
    'search_placeholder': 'Search for posts',
  }
  return render(request, 'core/display_post_details.html', context=context)


def display_found_posts(request, search_query):
  if request.method == 'GET':

    context = {
      'posts': Post.objects.all(),
      'search_placeholder': 'Search for posts',
    }
    return render(request, 'core/display_posts.html', context=context)


# ------------------------------------------------------------------------- TAG SECTION


def display_tags(request):
  context = {
    'tags': Tag.objects.all(),
    'path': get_path(request),
    'search_placeholder': 'Search for tags',
  }
  return render(request, 'core/display_tags.html', context=context)


def create_tag(request):
  if request.method == 'GET':
    context = {
      'form': TagCreationForm,
      'path': get_path(request),
      'search_placeholder': 'Search for tags',
    }
    return render(request, 'core/tag_creation_form.html', context=context)

  if request.method == 'POST':
    form = TagCreationForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('display_tags')

    else:
      context = {
        'form': form,
        'path': get_path(request),
        'search_placeholder': 'Search for tags',
      }
      return render(request, 'core/tag_creation_form.html', context=context)


def display_associated_posts(request, slug):
  tag = Tag.objects.get(slug__iexact=slug)
  context = {
    'tag_title': tag.title,
    'associated_posts': tag.posts.all(),
    'path': get_path(request),
    'search_placeholder': 'Search for posts',
  }
  return render(request, 'core/display_associated_posts.html', context=context)
