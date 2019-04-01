from django.forms import ModelForm
from django import  forms
from academy.models.event import Event
from academy.models.academy import Academy
from django.forms.widgets import Select
from django.forms.widgets import CheckboxInput


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["start"].widget = forms.TextInput(attrs={'data-toggle': 'flatpickr',})
        del self.fields["state"]
        self.fields["academy"].widget = Select()
        self.fields["academy"].queryset = Academy.objects.all()