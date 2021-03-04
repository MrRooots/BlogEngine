from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.shortcuts import reverse
from .models import Post, Tag


class PostCreationForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = [
      'title', 'text', 'tags'
    ]
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control mt-1 mb-4'}),
      'text': forms.Textarea(attrs={'class': 'form-control mt-1 mb-4', 'style': 'height: 150px'}),
      'tags': forms.CheckboxSelectMultiple(choices=Tag.objects.all(), attrs={'class': 'form-check'}),
    }


class TagCreationForm(forms.ModelForm):
  class Meta:
    model = Tag
    fields = [
      'title',
    ]
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control mt-1 mb-4'}),
    }

  def clean_title(self):
    title = self.cleaned_data.get('title').title()
    tag = Tag.objects.filter(title__iexact=title)

    if tag.count():
      link = f'<a href="{reverse("display_associated_posts", args=[tag[0].slug])}">{tag[0].title}</a>'
      raise ValidationError(mark_safe(f'This tag is already exist! You can find it here: {link} tag.'), code='invalid')

    return title
