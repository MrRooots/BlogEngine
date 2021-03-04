from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def create_slug(title):
  return f'{slugify(title)}-{str(time())[-7::]}'


def create_tag_slug(title):
  return f'tag-{slugify(title)}'


# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100, db_index=True, blank=False)
  slug = models.SlugField(max_length=100, unique=True, blank=True)
  text = models.TextField(blank=False)
  creation_date = models.DateTimeField(auto_now_add=True, blank=False)
  tags = models.ManyToManyField('Tag',  related_name='posts', blank=True)

  def get_tags_count(self):
    return self.tags.all().count()

  def get_absolute_url(self):
    return reverse('display_post_details', kwargs={'slug': self.slug})

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    self.slug = create_slug(self.title)
    self.title = self.title.title()

    return super().save(self, *args, **kwargs)


class Tag(models.Model):
  title = models.CharField(max_length=50, blank=False, unique=True)
  slug = models.SlugField(max_length=50, blank=True, unique=True)

  def get_absolute_url(self):
    return reverse('display_associated_posts', kwargs={'slug': self.slug})

  def save(self, *args, **kwargs):
    self.slug = create_tag_slug(self.title)
    self.title = self.title.strip().title()

    return super().save(self, *args, **kwargs)

  def __str__(self):
    return self.title
