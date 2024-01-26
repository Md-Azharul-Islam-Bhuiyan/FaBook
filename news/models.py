from django.db import models
from django.contrib.auth.models import User

class NewsCategory(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(NewsCategory, on_delete = models.CASCADE, null=True, blank=True)
    posted_user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='news/media/images/',blank=True, null=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title