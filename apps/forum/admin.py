from django.contrib import admin
from attachments.admin import AttachmentInlines
from .models.thread import Thread, ThreadTag, Comment
from .models.forum import Forum

class ThreadAdmin(admin.ModelAdmin):
    menu_group = "Forum"
    menu_title = "Thread"
    list_display = ['title', 'body', 'forum']

class ThreadTagAdmin(admin.ModelAdmin):
    menu_group = "Forum"
    menu_title = "Thread Tag"
    list_display = ['name', 'description']

class CommentAdmin(admin.ModelAdmin):
    menu_group = "Forum"
    menu_title = "Thread Comment"
    list_display = ['author', 'thread', 'body']

class ForumAdmin(admin.ModelAdmin):
    menu_group = "Forum"
    menu_title = "Forum"
    list_display = ['name', 'description']


admin.site.register(Thread, ThreadAdmin)
admin.site.register(ThreadTag, ThreadTagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Forum, ForumAdmin)

