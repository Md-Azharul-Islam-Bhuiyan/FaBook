from django.db import models

from django.contrib.auth.models import User


class PostModel(models.Model):
    title=models.CharField(max_length=50)
    posted_user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0) 
    dislike = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="book/media/images/",blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE,related_name='comments',null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post.title
    

class LikePost(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    like_post = models.IntegerField(default=0)
    is_like = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} Liked {self.post.title}"
    
    class Meta:
        verbose_name_plural = "LikePosts"
    
class DisLikePost(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    dislike_post = models.IntegerField(default=0)
    is_dislike = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.user.username} DisLiked {self.post.title}"
    
    class Meta:
        verbose_name_plural = "DisLikePosts"









    