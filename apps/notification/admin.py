from django.contrib import admin
from .models import notification

class NotificationAdmin(admin.ModelAdmin):
    menu_title = "Notification"
    menu_group = "Notification"
    list_display = ['title', 'type', 'message', 'sender', 'receiver', 'time', 'read', 'url' ]

admin.site.register(notification.Notification, NotificationAdmin)