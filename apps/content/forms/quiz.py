from django.forms import ModelForm
from content.models.quiz import QuizQuestion, ParticipantAnswer
from django.forms.widgets import Select

class QuizQuestionForm(ModelForm):
    class Meta:
        model = QuizQuestion
        exclude = []

