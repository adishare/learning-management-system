from django.contrib import admin
from .models import city
from .models import building
from .models import room
from .models import location
from .models import company

class CityAdmin(admin.ModelAdmin):
    menu_title = "City"
    menu_group = "Location"
    list_display = ['code', 'name', 'company' ]

class BuildingAdmin(admin.ModelAdmin):
    menu_title = "Building"
    menu_group = "Location"
    list_display = ['code', 'name', 'city', 'location', 'address', 'company' ]

class RoomAdmin(admin.ModelAdmin):
    menu_title = "Room"
    menu_group = "Location"
    list_display = ['code', 'name', 'building', 'city', 'company']

class LocationAdmin(admin.ModelAdmin):
    menu_title = "Location"
    menu_group = "Location"
    list_display = ['code', 'name', 'city', 'address' , 'company' ]    

class CompanyAdmin(admin.ModelAdmin):
    menu_title = "Company"
    menu_group = "Location"
    list_display = ['code', 'company_name', 'type'] 

admin.site.register(city.City, CityAdmin)
admin.site.register(building.Building, BuildingAdmin)
admin.site.register(room.Room, RoomAdmin)
admin.site.register(location.Location, LocationAdmin)
admin.site.register(company.Company, CompanyAdmin)

