from django.urls import path
from landing.views import curriculum
from competency.views import curriculum

urlpatterns = [
    path('', curriculum.index, name="landing-curriculum-index"),
    path('add/', curriculum.add, name="competency-curriculum-add"),
    path('<id>/edit/', curriculum.edit, name="competency-curriculum-edit"),
    path('<id>/delete/', curriculum.delete, name="competency-curriculum-delete"),
    path('<id>/', curriculum.view, name="competency-curriculum-view"),
    path('<id>/add-learnig-activity/', curriculum.add_learning_activity, name="competency-curriculum-add-learning-activity"),
    path('<id>/remove-learnig-activity/<learningActivityId>/', curriculum.remove_learning_activity, name="competency-curriculum-remove-learning-activity"),
]