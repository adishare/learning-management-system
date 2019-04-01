from django.contrib import admin
from .models import academy
from .models import partner
from .models import content_creator
from .models import event
from .models import strategic_plan
from .models import learning_plan
from .models import participant_event
from .models import learning_activity
from .models import event_plan
from attachments.admin import AttachmentInlines

class StrategicPlanIssueInline(admin.TabularInline):
    model = strategic_plan.StrategicPlanIssue

class AcademyAdmin(admin.ModelAdmin):
    menu_title = "Academy"
    menu_group = "Academy"
    autocomplete_fields = ['division',]
    list_display = ['code', 'name', 'company' ]

class PartnerAdmin(admin.ModelAdmin):
	menu_title = "Partner"
	menu_group = "Academy"
	list_display = ['code', 'name', 'type', 'company']

class ContentCreatorAdmin(admin.ModelAdmin):
	menu_title = "Content Creator"
	menu_group = "Academy"
	list_display = ['event', 'academy', 'start', 'end','type', 'learning_activity', 'resource', 'status', 'class_type', 'concealed']
		
class EventAdmin(admin.ModelAdmin):
    menu_title = "Event"
    menu_group = "Academy"
    list_display = ['event', 'learning_plan','curriculum_title', 'location', 'academy', 'start', 'type', 'classic_type', 'state', 'modified']

class EventPlanAdmin(admin.ModelAdmin):
    menu_title = "Event Plan"
    menu_group = "Academy"
    list_display = ['learning_plan', 'curriculum_title', 'mentor_request', 'vendor_request', 'start', 'end']

class StrategicPlan(admin.ModelAdmin):
    menu_title = "Strategic Plan"
    menu_group = "Academy"
    list_display = ['strategic_initiative',]
    inlines = [StrategicPlanIssueInline,]		

class LearningPlan(admin.ModelAdmin):
    menu_title = "Learning Plan"
    menu_group = "Academy"
    list_display = ['title', 'location', 'date', 'budget', 'competency_issue', 'participant', 'batch']

class ParticipantEventAdmin(admin.ModelAdmin):
    menu_title = "Partcipant Event"
    menu_group = "Academy"
    list_display = ['participant_name', 'event_name', 'state']

class LearningActivityAdmin(admin.ModelAdmin):
	menu_title = "Learning Activity"
	menu_group = "Academy"
	list_display = ['code','title', 'description', 'cycle', 'link' ]
	inlines = (AttachmentInlines,)

class StrategicPlanFieldAdmin(admin.ModelAdmin):
    list_display = ['name', 'sequence', 'required']




admin.site.register(academy.Academy, AcademyAdmin)
admin.site.register(partner.Partner, PartnerAdmin)
admin.site.register(event.Event, EventAdmin)
admin.site.register(strategic_plan.StrategicPlan, StrategicPlan)
admin.site.register(content_creator.ContentCreator, ContentCreatorAdmin)
admin.site.register(learning_plan.LearningPlan, LearningPlan)
admin.site.register(participant_event.ParticipantEvent, ParticipantEventAdmin)
admin.site.register(learning_activity.LearningActivity, LearningActivityAdmin)
admin.site.register(strategic_plan.StrategicPlanField, StrategicPlanFieldAdmin)
admin.site.register(event_plan.EventPlan, EventPlanAdmin)