from django.urls import path
from landing.views import student

urlpatterns = [
    path('', student.index, name="landing-student-index"),
]