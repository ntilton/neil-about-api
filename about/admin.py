from django.contrib import admin
from .models import Company, Role, Duty, Skill

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'blurb', 'dateStart', 'dateEnd')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'title', 'dateStart', 'dateEnd')

class DutyAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_company', 'get_role', 'description')

    @admin.display(description='Company')
    def get_company(self, obj):
        return obj.role.company

    @admin.display(description='Role')
    def get_role(self, obj):
        return obj.role.title

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(Skill, SkillAdmin)