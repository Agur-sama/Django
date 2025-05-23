# from django.contrib import admin
# from .models import Employee, Project, Participation

# admin.site.register(Employee)
# admin.site.register(Project)
# admin.site.register(Participation)


from django.contrib import admin
from .models import Employee, Project, Participation

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'position')
    search_fields = ('last_name', 'first_name', 'inn')
    list_filter = ('position',)
    
    # Русские названия полей
    fieldsets = [
        ('Основная информация', {
            'fields': [('last_name', 'first_name', 'middle_name'), 'position']
        }),
        ('Документы', {
            'fields': [('passport_series', 'passport_number'), 'inn', 'birth_date']
        }),
    ]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'budget')
    date_hierarchy = 'start_date'

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project', 'role')
    list_filter = ('project', 'role')

# Русские названия в админке
admin.site.site_header = "Администрирование НИИ"
admin.site.site_title = "Панель управления НИИ"
admin.site.index_title = "Управление данными"
admin.site.site_header = ('Администрирование сайта')
admin.site.index_title = ('Администрирование')