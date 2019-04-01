from django_undeletable.models import BaseModel
from django.utils.text import slugify
from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class ArticleCategory(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Article(BaseModel):
    STATE = (
        ("D", "Draft"),
        ("P", "Publish"),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    author = models.ForeignKey('account.User', on_delete=models.CASCADE)
    state = models.CharField(max_length=1, choices=STATE, default="D")
    body = RichTextUploadingField()
    category = models.ManyToManyField('ArticleCategory', blank=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    competency = models.ForeignKey('competency.Competency', on_delete=models.SET_NULL, blank=True, null=True)
    proficiency = models.ForeignKey('competency.Proficiency', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title

    def set_publish(self):
        if self.state == "D":
            now = timezone.now()
            self.state = "P"
            self.publish_date = now
            self.save()

    def set_draft(self):
        if self.state == "P":
            self.state = "D"
            self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = "%s-%s" % (self.id, slugify(self.title))
        self.set_publish() # auto publish for development env
        super().save(*args, **kwargs)

class ArticleComment(BaseModel):
    author = models.ForeignKey('account.User', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.body