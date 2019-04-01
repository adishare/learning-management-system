from django.urls import path
from academy.views import learning_activity

urlpatterns = [
    path('', learning_activity.index, name="academy-learning-activity-index"),
    path('add/', learning_activity.add, name="academy-learning-activity-add"),
    path('<id>/', learning_activity.view, name="academy-learning-activity-view"),
    path('<id>/edit/', learning_activity.edit, name="academy-learning-activity-edit"),
    path('<id>/delete/', learning_activity.delete, name="academy-learning-activity-delete"),
]
