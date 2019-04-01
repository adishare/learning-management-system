from django.urls import path
from content.views import article, quiz

urlpatterns = [
    path('article/', article.index, name="content-article-index"),
    path('article/<slug>', article.view, name="content-article-view"),
    path('article/<slug>/edit', article.edit, name="content-article-edit"),
    path('article/add/', article.add, name="content-article-add"),

    path('quiz/', quiz.index, name="content-quiz-index"),
    path('quiz/add/', quiz.add, name="content-quiz-add"),
    path('quiz/<id>/', quiz.view, name="content-quiz-view"),
    path('quiz/<id>/edit/', quiz.edit, name="content-quiz-edit"),
]
