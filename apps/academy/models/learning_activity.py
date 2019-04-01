from django_undeletable.models import BaseModel
from django.db import models


class LearningActivity(BaseModel):
        
    CYCLE_CHOICE = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
		(6, 6),
	)

    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    cycle = models.IntegerField(choices=CYCLE_CHOICE)
    competency = models.ManyToManyField("competency.Competency", blank=True)
    link = models.URLField(blank=True, null=True)
    articles = models.ManyToManyField("content.Article",blank=True)
    forum = models.ManyToManyField("forum.Forum", blank=True)
    quiz = models.ManyToManyField("content.QuizQuestion", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["cycle"]