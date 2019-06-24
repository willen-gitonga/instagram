from .models import Post, Comments,Profile
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
        model=Comments
        exclude=['user','images', 'description']


