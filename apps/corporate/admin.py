from django.contrib import admin
from .models import learning_focus

class LearningFocusAdmin(admin.ModelAdmin):
	menu_group = "Corporate"
	menu_title = "Learning Focus"
	list_display = [
        'unit_business','academy','year','org_competence','objective',
        'staff','supervisor','manager','senior_manager','top_management'
    ]

admin.site.register(learning_focus.LearningFocus, LearningFocusAdmin)