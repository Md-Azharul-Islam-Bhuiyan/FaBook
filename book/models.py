from django.db import models

from django.contrib.auth.models import User


class PostModel(models.Model):
    title=models.CharField(max_length=50)
    image = models.ImageField(upload_to="book/media/images/",blank=True, null=True)
    posted_user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0) 
    dislike = models.IntegerField(default=0)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.posted_user.username
    

class Comment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE,related_name='comments',null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class LikePost(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    like_post = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Liked {self.post.post_name}"
    
    class Meta:
        verbose_name_plural = "LikePosts"
    
class DisLikePost(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    dislike_post = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} DisLiked {self.book.book_name}"
    
    class Meta:
        verbose_name_plural = "DisLikePosts"





    