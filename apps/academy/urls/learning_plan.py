from django.urls import path
from academy.views import learning_plan

urlpatterns = [
    path('', learning_plan.index, name="academy-learning-plan-index"),
    path('add/', learning_plan.add, name="academy-learning-plan-add"),
    path('<id>/edit/', learning_plan.edit, name="academy-learning-plan-edit"),
    path('<id>/delete/', learning_plan.delete, name="academy-learning-plan-delete"),
]
