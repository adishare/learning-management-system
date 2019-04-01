from django_undeletable.models import BaseModel
from django.utils import timezone
from django.db import models

OPTION = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
)

class QuizQuestion(BaseModel):
    title = models.CharField(max_length=255)
    question = models.TextField()
    option_a = models.CharField(max_length=255, blank=True, null=True)
    option_b = models.CharField(max_length=255, blank=True, null=True)
    option_c = models.CharField(max_length=255, blank=True, null=True)
    option_d = models.CharField(max_length=255, blank=True, null=True)
    correct_option = models.CharField(max_length=1, choices=OPTION)
    competency = models.ManyToManyField('competency.Competency', blank=True)
    proficiency = models.ManyToManyField('competency.Proficiency', blank=True)

    def __str__(self):
        return self.title

class ParticipantAnswer(BaseModel):
    participant = models.ForeignKey('account.User', on_delete=models.CASCADE)
    question = models.OneToOneField('QuizQuestion', models.CASCADE)
    answer = models.CharField(max_length=1, choices=OPTION)
    text_answer = models.TextField(null=True, blank=True)
    score = models.IntegerField(blank=True, null=True)
    learning_plan = models.ForeignKey("academy.LearningPlan", on_delete=models.CASCADE, blank=True, null=True)

    def get_score(self):
        participant_answer = self.answer
        question_correct_option = self.question.correct_option
        if(participant_answer == question_correct_option):
            self.score = 100
            self.save()
        else:
            self.score = 0
            self.save()

    def __str__(self):
        return self.answer
