from django.forms import ModelForm
from django import forms
from academy.models.learning_plan import LearningPlan
from django.forms.widgets import DateInput

class LearningPlanForm(ModelForm):
    class Meta:
        model = LearningPlan
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].widget = DateInput(attrs={'data-toggle': 'flatpickr'})
