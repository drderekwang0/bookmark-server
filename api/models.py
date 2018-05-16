from django.db import models


class Bookmark(models.Model):
    title = models.TextField()
    url = models.TextField()
    time = models.DateTimeField()
    read = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
