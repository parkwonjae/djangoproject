from django.contrib import admin
from polls.models import Company
from polls.models import Employer
from polls.models import SelectAbility
from polls.models import EmployerQuestion
from polls.models import Compassion
from polls.models import SurfaceActing
from polls.models import DeepActing
from polls.models import AffectiveCommitment
from polls.models import TaskComplexity
from polls.models import IdentificationWithLeader
from polls.models import SelfEfficacy
from polls.models import JobSatisfaction
from polls.models import WillingnessToTakeRisks
from polls.models import Creativity
from polls.models import ComToEmployer

# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'company_name', 'company_establishment', 'company_size')
    search_fields = ('company_name', )


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'employer_id', 'employer_age', 'employer_gender', 'user')


@admin.register(SelectAbility)
class SelectAbilityAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'compassion', 'surface_acting', 'deep_acting', 'affective_commitment',
                    'task_complexity', 'identification_with_leader', 'self_efficacy', 'job_satisfaction',
                    'willingness_to_take_risks', 'creativity')


@admin.register(ComToEmployer)
class ComTOEmployer(admin.ModelAdmin):
    list_display = ('company_id', 'employer_id')


@admin.register(EmployerQuestion)
class EmployerQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'company_id', 'employer_id',
        'question_1', 'question_2', 'question_3', 'question_4',
        'question_5', 'question_6', 'question_7', 'question_8',
        'question_9', 'question_10', 'question_11', 'question_12',
        'question_13', 'question_14', 'question_15', 'question_16',
        'question_17', 'question_18', 'question_19', 'question_20',
    )


@admin.register(Compassion)
class CompassionAdmin(admin.ModelAdmin):
    list_display = (
        'ability', 'compassion_1', 'compassion_2', 'compassion_3'
    )


@admin.register(SurfaceActing)
class SurfaceActingAdmin(admin.ModelAdmin):
    list_display = (
        'ability', 'surface_acting_1', 'surface_acting_2', 'surface_acting_3',
        'surface_acting_4', 'surface_acting_5', 'surface_acting_6', 'surface_acting_7'
    )


@admin.register(DeepActing)
class DeepActingAdmin(admin.ModelAdmin):
    list_display = (
        'ability', 'deep_acting_1', 'deep_acting_2', 'deep_acting_3', 'deep_acting_4'
    )


@admin.register(AffectiveCommitment)
class AffectiveCommitmentAdmin(admin.ModelAdmin):
    list_display = (
        'ability', 'affective_commitment_1','affective_commitment_2','affective_commitment_3',
        'affective_commitment_4','affective_commitment_5','affective_commitment_6','affective_commitment_7',
        'affective_commitment_8'

    )


@admin.register(TaskComplexity)
class TaskComplexityAdmin(admin.ModelAdmin):
    list_display = (
        'ability', 'task_complexity_1', 'task_complexity_2', 'task_complexity_3'
    )


@admin.register(IdentificationWithLeader)
class IdentificationWithLeaderAdmin(admin.ModelAdmin):
    list_display = (
        'ability', 'identification_with_leader_1','identification_with_leader_2','identification_with_leader_3',
        'identification_with_leader_4', 'identification_with_leader_5'
    )


@admin.register(SelfEfficacy)
class SelfEfficacyAdmin(admin.ModelAdmin):
    list_display = (
        'ability', 'self_efficacy_1', 'self_efficacy_2', 'self_efficacy_3',
        'self_efficacy_4', 'self_efficacy_5', 'self_efficacy_6'
    )


@admin.register(JobSatisfaction)
class JobSatisfactionAdmin(admin.ModelAdmin):
    list_display = (
        'ability', 'job_satisfaction_1', 'job_satisfaction_2', 'job_satisfaction_3',
        'job_satisfaction_4', 'job_satisfaction_5'
    )


@admin.register(WillingnessToTakeRisks)
class WillingnessToTakeRisksAdmin(admin.ModelAdmin):
    list_display = (
        'ability', 'willingness_to_take_risks_1', 'willingness_to_take_risks_2', 'willingness_to_take_risks_3',
        'willingness_to_take_risks_4', 'willingness_to_take_risks_5'
    )


@admin.register(Creativity)
class CreativityAdmin(admin.ModelAdmin):
    list_display = (
        'ability', 'creativity_1', 'creativity_2', 'creativity_3',
        'creativity_4', 'creativity_5', 'creativity_6'
    )
