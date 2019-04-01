from django.contrib import admin
from attachments.admin import AttachmentInlines
from .models.article import Article, ArticleCategory
from .models.quiz import QuizQuestion, ParticipantAnswer
from import_export.admin import ImportExportModelAdmin


def action_set_publish(modeladmin, request, queryset):
    for article in queryset:
        article.set_publish()
action_set_publish.short_description = "Publish Article"

def action_set_draft(modeladmin, request, queryset):
    for article in queryset:
        article.set_draft()
action_set_draft.short_description = "Take Down Article"

def action_get_score(modeladmin, request, queryset):
    for participantanswer in queryset:
        participantanswer.get_score()
action_get_score.short_description = "Score Participant Answer"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date', 'state']
    actions = [action_set_publish,action_set_draft]
    readonly_fields = ['state', 'publish_date']
    inlines = (AttachmentInlines,)

# QUIZ
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'question','option_a', 'option_b', 'option_c', 'option_d', 'correct_option']

class ParticipantAnswerAdmin(admin.ModelAdmin):
    list_display = ['participant', 'question', 'answer', 'text_answer', 'score']
    actions = [action_get_score]
    readonly_fields = ['score']

class QuizResource(ImportExportModelAdmin):
    model = QuizQuestion

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
admin.site.register(QuizQuestion, QuizResource)
admin.site.register(ParticipantAnswer, ParticipantAnswerAdmin)
