from django.contrib import admin
from .models import competency
from .models import competency_requirement
from .models import curriculum
from .models import proficiency
from .models import employee_competency

class CompetencyAdmin(admin.ModelAdmin):
    menu_title = "Competency"
    menu_group = "Competency"
    list_display = ['title', 'parent', 'company' ]

class CompetencyRequirementAdmin(admin.ModelAdmin):
    menu_title = "Competency Requirement"
    menu_group = "Competency"
    list_display = ['competency', 'proficiency' , 'position', 'company']

class CurriculumAdmin(admin.ModelAdmin):
    menu_title = "Curriculum"
    menu_group = "Competency"
    list_display = ['title', 'competency_goal', 'capacity', 'claim', 'company']

class ProficiencyAdmin(admin.ModelAdmin):
    menu_title = "Proficiency"
    menu_group = "Competency"
    list_display = [ 'level', 'company']

class EmployeeCompetencyAdmin(admin.ModelAdmin):
    menu_title = "Employee Competency"
    menu_group = "Competency"
    list_display = ['employee', 'competency', 'proficiency', 'company'] 

admin.site.register(competency.Competency, CompetencyAdmin)
admin.site.register(competency_requirement.CompetencyRequirement, CompetencyRequirementAdmin)
admin.site.register(curriculum.Curriculum, CurriculumAdmin)
admin.site.register(proficiency.Proficiency, ProficiencyAdmin)
admin.site.register(employee_competency.EmployeeCompetency, EmployeeCompetencyAdmin)
