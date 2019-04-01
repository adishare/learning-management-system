from django import forms
from academy.models.strategic_plan import StrategicPlan, StrategicPlanField, StrategicPlanIssue
from academy.models.academy import Academy
from django.forms.widgets import Select

class StrategicPlanForm(forms.ModelForm):
    class Meta:
        model = StrategicPlan
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in StrategicPlanField.objects.exclude(name="Strategic Initiative").order_by("sequence"):
            field_name = field.name.lower().replace(" ", "_") 
            self.fields[field_name] = forms.CharField(required=field.required)
            if 'instance' in kwargs:
                try:
                    content = kwargs['instance'].strategicplanissue_set.get(name=field_name)
                    self.initial[field_name] = content.content
                except StrategicPlanIssue.DoesNotExist:
                    pass
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        data = dict(self.cleaned_data)
        del data['strategic_initiative']
        for item in data.items():
            StrategicPlanIssue.objects.update_or_create(
                strategic_plan=self.instance,
                name=item[0],
                defaults={
                    "strategic_plan": self.instance,
                    "name": item[0],
                    "content": item[1]})
