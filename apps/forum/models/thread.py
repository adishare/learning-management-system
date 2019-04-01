from django_undeletable.models import BaseModel
from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class ThreadTag(BaseModel):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Thread(BaseModel):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('account.User', on_delete=models.CASCADE)
    body = models.TextField()
    tag = models.ManyToManyField('ThreadTag', blank=True)
    forum = models.ForeignKey("forum.Forum", blank=True, null=True ,on_delete=models.SET_NULL)

    def get_comments(self):
        return Comment.objects.filter(thread__pk=self.pk)
    
    def __str__(self):
        return self.title


class Comment(BaseModel):
    author = models.ForeignKey('account.User', on_delete=models.CASCADE)
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.body