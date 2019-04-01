from django.forms import ModelForm
from django import forms
from academy.models.learning_activity import LearningActivity
from competency.models.competency import Competency
from django.forms.widgets import CheckboxSelectMultiple

class LearningActivityForm(ModelForm):
    class Meta:
        model = LearningActivity
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["competency"].widget = CheckboxSelectMultiple()
        self.fields["competency"].queryset = Competency.objects.all()