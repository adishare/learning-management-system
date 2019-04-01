from django.urls import path, include
from competency.views import curriculum

urlpatterns = [
    path('add/', curriculum.add, name="competency-curriculum-add"),
    path('edit/', curriculum.edit, name="competency-curriculum-edit"),
    path('<id>/', curriculum.view, name="competency-curriculum-view"),
]