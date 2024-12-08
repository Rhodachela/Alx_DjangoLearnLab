from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagField
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.forms.widgets import TextInput, Textarea
from taggit.forms import TagWidget  # Ensure this line is included


class PostForm(forms.ModelForm):
    tags = TaggableManager(
        help_text="Separate tags with spaces.",
        # Using TagWidget to enable better UX for tagging
        widget=TagWidget(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }
