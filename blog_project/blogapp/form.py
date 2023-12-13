from django import forms
from .models import Post,Comment

class AddPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body']


class EditPostForm(AddPostForm):pass

class AddComment(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment_text']
