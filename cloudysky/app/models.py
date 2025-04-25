from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.conf import settings

class Usertype(models.Model):
    name = models.CharField(max_length=32, unique=True)

class Users(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    usertype = models.ForeignKey(Usertype, on_delete=models.PROTECT)
    bio = models.TextField()
    avatar = models.ForeignKey('Media', null=True, on_delete=models.SET_NULL)

class Post(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    is_suppressed = models.BooleanField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    is_suppressed = models.BooleanField()

class Media(models.Model):
    AVATAR = 'avatar'
    POST_IMAGE = 'post_image'
    COMMENT_IMAGE = 'comment_image'
    TYPE_CHOICES = [
        (AVATAR, 'Avatar'),
        (POST_IMAGE, 'Post Image'),
        (COMMENT_IMAGE, 'Comment Image'),
    ]

    uploaded_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=AVATAR)
    file = models.FileField(upload_to='media/')
    attached_post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    attached_comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)