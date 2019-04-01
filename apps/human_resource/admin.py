from django.contrib import admin
from .models import employee
from .models import employee_grade
from .models import division
from .models import position
from .models import workplace
from .models import participant

class EmployeeAdmin(admin.ModelAdmin):
	menu_group = "People"
	menu_title = "Employee"
	list_display = ['company', 'location', 'division', 'position', 
                    'ic_number', 'name', 'email', 'address', 'phone','grade']

class EmployeeGradeAdmin(admin.ModelAdmin):
    menu_group = "People"
    menu_title = "Employee Level"
    list_display = ['company', 'title', 'description']
    def has_add_permission(self, request):
        return False

class DivisionAdmin(admin.ModelAdmin):
    search_fields = ['code', 'name']
    menu_group = "People"
    menu_title = "Division"
    list_display = ['company', 'code', 'name']

class PositionAdmin(admin.ModelAdmin):
    menu_group = "People"
    menu_title = "Position"
    list_display = ['company', 'code', 'title']

class WorkplaceAdmin(admin.ModelAdmin):
    menu_group = "People"
    menu_title = "Workplace"
    list_display = ['company', 'division', 'code', 'name']

class ParticipantAdmin (admin.ModelAdmin):
    menu_group = "People"
    menu_tite = "Participant"
    list_display = ['nik', 'name', 'age', 'address', 'telephone_number', 'created']

admin.site.register(division.Division, DivisionAdmin)
admin.site.register(position.Position, PositionAdmin)
admin.site.register(employee.Employee, EmployeeAdmin)
admin.site.register(employee_grade.EmployeeGrade, EmployeeGradeAdmin)
admin.site.register(workplace.Workplace, WorkplaceAdmin)
admin.site.register(participant.Participant, ParticipantAdmin)
