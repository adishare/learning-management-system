from django_undeletable.models import BaseModel
from django.db import models

class Testimonial(BaseModel):
    TESTIMONIAL_CATEGORY=(
        ('Management', "Management"),
        ('Course', "Course"),
        ('Instructor', "Instructor"),
    )

    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    event = models.ForeignKey('academy.Event', on_delete=models.CASCADE)
    category = models.ForeignKey('TestimonialCategory', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Questionnaire(BaseModel):
    code = models.CharField(max_length=225)
    event = models.ForeignKey('academy.Event', on_delete=models.CASCADE)
    category = models.ForeignKey('QuestionnaireCategory', on_delete=models.CASCADE)
    question = models.CharField(max_length=225)

    def __str__(self):
        return self.question

class QuestionnaireAnswer(BaseModel):
    question = models.ForeignKey('feedback.Questionnaire', on_delete=models.CASCADE)
    answer = models.CharField(max_length=225)

    def __str__(self):
        return self.answer

class QuestionnaireCategory(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TestimonialAnswer(BaseModel):
    question = models.ForeignKey('feedback.Testimonial', on_delete=models.CASCADE)
    answer = models.CharField(max_length=225)

    def __str__(self):
        return self.answer

class TestimonialCategory(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
