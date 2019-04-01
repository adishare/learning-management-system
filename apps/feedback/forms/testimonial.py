from django.forms import ModelForm
from feedback.models.feedback import Testimonial, TestimonialAnswer

class TestimonialForm(ModelForm):
    class Meta:
        model = TestimonialAnswer
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)