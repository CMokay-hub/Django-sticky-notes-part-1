from django.db import models


class Post(models.Model):
    """Model representing a post in the bulletin board.

    Fields:
    - title: CharField to store the title of the post.
    - content: TextField to store the content of the post.
    - created_at: DateTimeField to store the current date and
    time of the post.

    Relationships:
    - author: ForeignKey to the User model, representing the
    author of the post.

    Methods:
    - __str__: Returns a string representation of the post,
    which is the title of the post.

    :param models.Model: The base class for all Django models.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Define a ForeignKey relationship to the User model, representing the
    # author of the post. The on_delete=models.CASCADE argument ensures that
    # if a user is deleted, all their posts will also be deleted.
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, null=True, blank=True
        )

    def __str__(self):
        """Return a string representation of the post."""
        return self.title


class Author(models.Model):
    """Model representing an author of a post.

    Fields:
    - name: CharField to store the name of the author.

    Methods:
    - __str__: Returns a string representation of the author,
    which is the name of the author.

    :param models.Model: The base class for all Django models.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        """Return a string representation of the author."""
        return self.name
