from django.db import models
from categories.models import Category


class Site(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField()
    img = models.CharField(max_length=1000)
    category = models.ForeignKey(
        to=Category,
        related_name="sites",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title[:20]


class Likes(models.Model):
    num = models.IntegerField()
    likes = models.ForeignKey(
        to=Site,
        related_name="likes",
        on_delete=models.CASCADE
    )
