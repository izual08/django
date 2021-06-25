from django.db import models
from django.utils import timezone

class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    pubdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.pubdate} - {self.name}"
