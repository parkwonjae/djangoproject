from django.contrib import admin
from polls.models import SelectVariable


# Register your models here.

@admin.register(SelectVariable)
class SelectVariableAdmin(admin.ModelAdmin):
    list_display = ('id', 'co_id', 'compassion', 'surface_acting', 'deep_acting',
                    'affective_commitment', 'task_complexity')
    search_fields = ('co_id',)
