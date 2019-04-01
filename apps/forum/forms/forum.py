from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from forum.models.forum import Forum

class ForumForm(ModelForm):
    class Meta:
        model = Forum
        exclude = ['members']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["competency"].widget = CheckboxSelectMultiple()
        self.fields["proficiency"].widget = CheckboxSelectMultiple()