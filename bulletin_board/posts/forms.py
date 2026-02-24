# posts/forms.py
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Form for creating and updating Post objects.

    Fields:
    - title: CharField for the title of the post.
    - content: TextField for the content of the post.

    Meta class:
    - Defines the model to be used (Post) and the fields
    to be included in the form.

    :param forms.ModelForm: The base class for creating forms
    based on Django models.
    """
    class Meta:
        model = Post
        fields = ["title", "content", "author"]
