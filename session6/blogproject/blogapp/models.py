from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.TextField()
    time = models.DateTimeField(auto_now=True)
    
def __str__(self):
    return self.title