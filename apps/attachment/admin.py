from django.contrib import admin
from .models import attachment

class AttachmentAdmin(admin.ModelAdmin):
	menu_title = "Attachment"
	menu_group = "Attachment"
	list_display = ['begin_date', 'end_date', 'name', 'cycle','format',
					'description', 'file', 'content_type', 'objid']

admin.site.register(attachment.Attachment, AttachmentAdmin)