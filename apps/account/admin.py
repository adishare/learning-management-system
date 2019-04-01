from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Role


class CustomUserAdmin(UserAdmin):
    readonly_fields = ["last_login", "date_joined"]
    list_display = ['username', 'full_name', 'active_role','last_login']
    autocomplete_fields = ['groups',]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("full_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "role",
                    'active_role',
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

# class GroupAdmin(admin.ModelAdmin):
#     search_fields = ['name']
#     menu_group = "Role"
#     list_display = ['name', ]

class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Role, RoleAdmin)
# admin.site.unregister(Group)
# admin.site.register(Group, GroupAdmin)