from django.contrib import admin
from polls.models import SelectVariable
from polls.models import Employee


# Register your models here.


@admin.register(SelectVariable)
class SelectVariableAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_id', 'compassion', 'surface_acting', 'deep_acting',
                    'affective_commitment', 'task_complexity')
    search_fields = ('company_id',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_id', 'compassion_1', 'compassion_2', 'surface_acting_1', 'surface_acting_2',
                    'deep_acting_1', 'deep_acting_2', 'affective_commitment_1', 'affective_commitment_2',
                    'task_complexity_1', 'task_complexity_2')
    search_fields = ('company_id',)
