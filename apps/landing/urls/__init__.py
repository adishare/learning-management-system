from django.urls import path, include

urlpatterns = [
    path('student/', include("landing.urls.student")),
    path('expert/', include("landing.urls.expert")),
    path('content-creator/', include("landing.urls.content_creator")),
    path('curriculum/', include("landing.urls.curriculum")),
    path('content-creator/', include("landing.urls.content_creator")),
    path('plan-manager/', include("landing.urls.plan_manager")),
    path('event-manager/', include("landing.urls.event_manager")),
     path('event-plan/', include("landing.urls.event_plan")),
    path('mentor/', include("landing.urls.mentor")),
]