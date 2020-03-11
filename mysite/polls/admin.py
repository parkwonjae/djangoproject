from django.contrib import admin
from polls.models import SelectVariable
from polls.models import Employee


# Register your models here.


@admin.register(SelectVariable)
class SelectVariableAdmin(admin.ModelAdmin):
    list_display = ('id', 'co_id', 'compassion', 'surface_acting', 'deep_acting',
                    'affective_commitment', 'task_complexity')
    search_fields = ('co_id',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_id', 'employee_pw', 'employee_coname', 'co_id')
    search_fields = ('employee_id', 'employee_coname', 'co_id', 'id')
