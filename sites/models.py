from django.db import models

# Create your models here.


class Site(models.Model):
    title = models.CharField(max_length=200)
    inf = models.TextField()
    img = models.CharField(max_length=1000)
    category = models.ForeignKey(
        to=Category,
        related_name="sites",
        on_delete=models.CASCADE()
    )

    def __str__(self):
        return self.title[:20]
