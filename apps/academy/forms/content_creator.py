from django.forms import ModelForm
from academy.models.content_creator import ContentCreator
from academy.models.academy import Academy
from django.forms.widgets import Select, DateInput

class ContentCreatorForm(ModelForm):
    class Meta:
        model = ContentCreator
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["academy"].widget = Select()
        self.fields["academy"].queryset = Academy.objects.all()
        self.fields["start"].widget = DateInput(attrs={'type':'date', 'data-toggle': 'flatpickr'})
        self.fields["end"].widget = DateInput(attrs={'type':'date', 'data-toggle': 'flatpickr'})