from django.urls import path, include
from landing.views import strategic_plan
from academy.views import learning_plan

urlpatterns = [
    path('strategic-plan/', strategic_plan.index, name="landing-strategic-plan-index"),
    path('strategic-plan/add/', strategic_plan.add, name="landing-strategic-plan-add"),
    path('strategic-plan/<id>/edit/', strategic_plan.edit, name="landing-strategic-plan-edit"),
    path('strategic-plan/<id>/delete/', strategic_plan.delete, name="landing-strategic-plan-delete"),
    # path('learning-plan/', include("academy.urls.learning_plan")),
    path('learning-plan/', learning_plan.index, name="academy-learning-plan-index"),
    path('learning-plan/add/', learning_plan.add, name="academy-learning-plan-add"),
    path('learning-plan/<id>/edit/', learning_plan.edit, name="academy-learning-plan-edit"),
    path('learning-plan/<id>/delete/', learning_plan.delete, name="academy-learning-plan-delete"),
]