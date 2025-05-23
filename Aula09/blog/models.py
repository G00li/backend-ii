from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def get_summary(self, max_length=100):
        if len(self.content) <= max_length:
            return self.content
        return self.content[:max_length] + "..." 