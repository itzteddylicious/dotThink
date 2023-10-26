from django.contrib.auth.models import User
from django.db import models


class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    favorites = models.ManyToManyField(User, default=None, blank=True, related_name='favorite')

    def __str__(self):
        return self.title
    
