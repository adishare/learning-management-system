from django.urls import path, include
from landing.views import content_creator

urlpatterns = [
    path('', content_creator.index, name="landing-content-creator-index"),
    path('add/', content_creator.add, name="landing-content-creator-add"),
    path('<id>/edit/', content_creator.edit, name="academy-content-creator-edit"),
    path('<id>/delete/', content_creator.delete, name="academy-content-creator-delete"),
]