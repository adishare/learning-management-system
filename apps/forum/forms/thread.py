from django.forms import ModelForm
from django.forms.widgets import Select
from forum.models.forum import Forum
from forum.models.thread import Thread

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["forum"].widget = Select()
        self.fields["forum"].queryset = Forum.objects.all()