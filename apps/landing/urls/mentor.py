from django.urls import path
from landing.views import mentor

urlpatterns = [
    path('', mentor.index, name="landing-mentor-index"),
    path('<id>/delete/', mentor.delete, name="mentor-delete"),
   
]