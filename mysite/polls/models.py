from django.db import models


# Create your models here.


class Company(models.Model):
    company_id = models.CharField(max_length=15)
    company_name = models.CharField(max_length=20, blank=False)
    company_establishment = models.IntegerField(blank=False)
    company_size = models.IntegerField(blank=False)


class Employer(models.Model):
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE())
    employer_id = models.CharField(max_length=15)
    employer_age = models.IntegerField()
    employer_sex = models.ChoiceField()


class Polls(models.Model):
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE())
    employ = models.ChoiceField()


# 인사담당자가 변수 선택한 테이블
class Variable(models.Model):
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE())
    employ = models.ForeignKey('Polls', on_delete=models.CASCADE())
    compassion = models.BooleanField(default=False)
    surface_acting = models.BooleanField(default=False)
    deep_acting = models.BooleanField(default=False)
    affective_commitment = models.BooleanField(default=False)
    task_complexity = models.BooleanField(default=False)
    identification_with_leader = models.BooleanField(default=False)
    self_efficacy = models.BooleanField(default=False)
    job_satisfaction = models.BooleanField(default=False)
    willingness_to_take_risks = models.BooleanField(default=False)
    creativity = models.BooleanField(default=False)


class Question(models.Model):
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE())
    employ = models.ForeignKey('Polls', on_delete=models.CASCADE())
    compassion = models.ForeignKey('Variable', on_delete=models.CASCADE())
    compassion_1 = models.ChoiceField()
    compassion_2 = models.ChoiceField()
    compassion_3 = models.ChoiceField()

    surface_acting = models.ForeignKey('Variable', on_delete=models.CASCADE())
    surface_acting_1 = models.ChoiceField()
    surface_acting_2 = models.ChoiceField()
    surface_acting_3 = models.ChoiceField()
    surface_acting_4 = models.ChoiceField()
    surface_acting_5 = models.ChoiceField()
    surface_acting_6 = models.ChoiceField()
    surface_acting_7 = models.ChoiceField()

    deep_acting = models.ForeignKey('Variable', on_delete=models.CASCADE())
    deep_acting_1 = models.ChoiceField()
    deep_acting_2 = models.ChoiceField()
    deep_acting_3 = models.ChoiceField()
    deep_acting_4 = models.ChoiceField()

    affective_commitment = models.ForeignKey('Variable', on_delete=models.CASCADE())
    affective_commitment_1 = models.ChoiceField()
    affective_commitment_2 = models.ChoiceField()
    affective_commitment_3 = models.ChoiceField()
    affective_commitment_4 = models.ChoiceField()
    affective_commitment_5 = models.ChoiceField()
    affective_commitment_6 = models.ChoiceField()
    affective_commitment_7 = models.ChoiceField()
    affective_commitment_8 = models.ChoiceField()

    task_complexity = models.ForeignKey('Variable', on_delete=models.CASCADE())
    task_complexity_1 = models.ChoiceField()
    task_complexity_2 = models.ChoiceField()
    task_complexity_3 = models.ChoiceField()

    identification_with_leader = models.ForeignKey('Variable', on_delete=models.CASCADE())
    identification_with_leader_1 = models.ChoiceField()
    identification_with_leader_2 = models.ChoiceField()
    identification_with_leader_3 = models.ChoiceField()
    identification_with_leader_4 = models.ChoiceField()
    identification_with_leader_5 = models.ChoiceField()
    identification_with_leader_6 = models.ChoiceField()

    self_efficacy = models.ForeignKey('Variable', on_delete=models.CASCADE())
    self_efficacy_1 = models.ChoiceField()
    self_efficacy_2 = models.ChoiceField()
    self_efficacy_3 = models.ChoiceField()
    self_efficacy_4 = models.ChoiceField()
    self_efficacy_5 = models.ChoiceField()
    self_efficacy_6 = models.ChoiceField()

    job_satisfaction = models.ForeignKey('Variable', on_delete=models.CASCADE())
    job_satisfaction_1 = models.ChoiceField()
    job_satisfaction_2 = models.ChoiceField()
    job_satisfaction_3 = models.ChoiceField()
    job_satisfaction_4 = models.ChoiceField()
    job_satisfaction_5 = models.ChoiceField()

    willingness_to_take_risks = models.ForeignKey('Variable', on_delete=models.CASCADE())
    willingness_to_take_risks_1 = models.ChoiceField()
    willingness_to_take_risks_2 = models.ChoiceField()
    willingness_to_take_risks_3 = models.ChoiceField()
    willingness_to_take_risks_4 = models.ChoiceField()
    willingness_to_take_risks_5 = models.ChoiceField()

    creativity = models.ForeignKey('Variable', on_delete=models.CASCADE())
    creativity_1 = models.ChoiceField()
    creativity_2 = models.ChoiceField()
    creativity_3 = models.ChoiceField()
    creativity_4 = models.ChoiceField()
    creativity_5 = models.ChoiceField()
    creativity_6 = models.ChoiceField()

    # employer questions
    question_1 = models.ChoiceField()
    question_2 = models.ChoiceField()
    question_3 = models.ChoiceField()
    question_4 = models.ChoiceField()
    question_5 = models.ChoiceField()
    question_6 = models.ChoiceField()
    question_7 = models.ChoiceField()
    question_8 = models.ChoiceField()
    question_9 = models.ChoiceField()
    question_10 = models.ChoiceField()
    question_11 = models.ChoiceField()
    question_12 = models.ChoiceField()
    question_13 = models.ChoiceField()
    question_14 = models.ChoiceField()
    question_15 = models.ChoiceField()
    question_16 = models.ChoiceField()
    question_17 = models.ChoiceField()
    question_18 = models.ChoiceField()
    question_19 = models.ChoiceField()
    question_20 = models.ChoiceField()
