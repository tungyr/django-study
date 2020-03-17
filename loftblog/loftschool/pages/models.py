from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)

    text = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):

    text = models.TextField()

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text
