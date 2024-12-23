from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    source = models.URLField()
    publication_date = models.DateTimeField()

class UserSearch(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    search_terms = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
