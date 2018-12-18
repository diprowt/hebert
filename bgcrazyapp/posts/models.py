"""Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('registration.Profile', on_delete=models.CASCADE)

    title = RichTextField(blank=True)
    photo = models.ImageField(
        upload_to='posts/photos',
        blank=True,
        null=True
    )


    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)

    def total_likes(self):
        return self.likes.count()

    # def get_absolute_url(self):
    #     return reverse("posts:detail" , args=[self.id , self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('registration.Profile', on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment' , null=True , related_name="replies", on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} by @{}'.format(self.post.title, str(self.user.username))
