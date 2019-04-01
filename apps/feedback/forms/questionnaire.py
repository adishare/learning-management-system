from django.forms import ModelForm
from feedback.models.feedback import Questionnaire, QuestionnaireAnswer

class QuestionnaireForm(ModelForm):
    class Meta:
        model = QuestionnaireAnswer
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)