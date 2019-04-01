from django.forms import ModelForm
from competency.models.curriculum import Curriculum
from academy.models.learning_activity import LearningActivity
from django.forms.widgets import Select

class CurriculumForm(ModelForm):
    class Meta:
        model = Curriculum
        exclude = ['learning_activity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
