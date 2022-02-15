from django import forms

from .models import Blog,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude=("author","likes")
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)