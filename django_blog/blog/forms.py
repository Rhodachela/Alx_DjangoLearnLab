from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagField

class PostForm(forms.ModelForm):
    tags = TagField(required=False)  # Enable tagging in forms

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }