"""Post forms."""

# Django
from django import forms

# Models
from posts.models import Post , Comment


class PostForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'', 'placeholder':'añade una respuesta'}))
    class Meta:
        model = Comment 
        fields = ('user','content')
