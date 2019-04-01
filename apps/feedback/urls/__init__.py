from django.urls import path
from feedback.views import testimonial
from feedback.views import questionnaire

urlpatterns = [
    path('testimonial/', testimonial.index, name="feedback-testimonial-index"),
    path('testimonial/view/', testimonial.view, name="feedback-testimonial-view"),
    path('testimonial/add/', testimonial.add, name="feedback-testimonial-add"),
    path('questionnaire/', questionnaire.index, name="feedback-questionnaire-index"),
    path('questionnaire/participant/', questionnaire.participant, name="feedback-questionnaire-participant-list"),
    path('questionnaire/add/', questionnaire.add, name="feedback-questionnaire-add"),
]
