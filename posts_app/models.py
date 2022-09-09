from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=500, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.name}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post')
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    date_liked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} liked your {self.post}"
