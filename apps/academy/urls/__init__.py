from django.urls import path, include

urlpatterns = [
    path('event/', include("academy.urls.event")),
    path('event-plan/', include("academy.urls.event_plan")),
    path('learning-activity/', include("academy.urls.learning_activity")),
    path('mentor/', include("academy.urls.mentor")),
]