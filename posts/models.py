from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    content = models.TextField()  # Content of the blog post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post is created

    def __str__(self):
        return self.title  # When querying posts, show the title in admin or shell
