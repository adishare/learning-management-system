from django.urls import path
from forum.views import thread, forum

urlpatterns = [
    path('thread/', thread.index, name="forum-thread-index"),
    path('thread/add/', thread.add, name="forum-thread-add"),
    path('thread/<id>/', thread.view, name="forum-thread-view"),
    path('thread/<id>/comment/add/', thread.add_comment, name="forum-thread-comment-add"),
    path('thread/<id>/edit/', thread.edit, name="forum-thread-edit"),
    path('thread/<id>/delete/', thread.delete, name="forum-thread-delete"),

    path('', forum.index, name="forum-index"),
    path('add/', forum.add, name="forum-add"),
    path('<id>/', forum.view, name="forum-view"),
    path('<id>/edit/', forum.edit, name="forum-edit"),
    path('<id>/addthread/', forum.addthread, name="forum-add-thread"),
]
