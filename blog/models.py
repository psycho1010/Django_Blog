from django.db import models
from django.contrib.auth.models import User  # Import User model

class Post(models.Model):
    title = models.CharField(max_length=200)  # Text field for post title
    content = models.TextField()  # Large text field for blog content
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # One-to-Many relation
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when post is created

    def __str__(self):
        return self.title  # Display title in admin panel
