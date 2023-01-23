from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return str(f"{self.writer} {self.id}")
    
    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])