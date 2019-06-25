from .models import Post, Comment,Profile
from django import forms
from django.forms import ModelForm, Textarea, IntegerField


class NewPostForm(forms.ModelForm):
  class Meta:
      model = Post
      exclude = ['comments','user']

class EditProfileForm(forms.ModelForm):
  class Meta:
      model=Profile
      exclude=['profile_name']

class UpdateProfileForm(forms.ModelForm):
  class Meta:
      model=Profile
      exclude=['profile_name']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['user','image']


