from django.db import models


# Create your models here.


class Company(models.Model):
    company_id = models.CharField(max_length=15)
    company_name = models.CharField(max_length=20, blank=False)
    company_establishment = models.IntegerField(blank=False)
    company_size = models.IntegerField(blank=False)


class Employer(models.Model):
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    employer_id = models.CharField(max_length=15)
    employer_age = models.IntegerField()
    gender_choices = (
        ('1', '남'),
        ('2', '여')
    )
    employer_gender = models.ChoiceField(choices=gender_choices)


class Polls(models.Model):
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    employ = models.ChoiceField(
        ('1', '인사담당자'),
        ('2', '일반사원')
    )


class Question(models.Model):
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    employ = models.ForeignKey('Polls', on_delete=models.CASCADE)
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


class Compassion(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    num_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    compassion_1 = models.ChoiceField(choices=num_choices)
    compassion_2 = models.ChoiceField(choices=num_choices)
    compassion_3 = models.ChoiceField(choices=num_choices)


class SurfaceActing(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    num_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    surface_acting_1 = models.ChoiceField(choices=num_choices)
    surface_acting_2 = models.ChoiceField(choices=num_choices)
    surface_acting_3 = models.ChoiceField(choices=num_choices)
    surface_acting_4 = models.ChoiceField(choices=num_choices)
    surface_acting_5 = models.ChoiceField(choices=num_choices)
    surface_acting_6 = models.ChoiceField(choices=num_choices)
    surface_acting_7 = models.ChoiceField(choices=num_choices)


class DeepActing(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    num_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    deep_acting_1 = models.ChoiceField(choices=num_choices)
    deep_acting_2 = models.ChoiceField(choices=num_choices)
    deep_acting_3 = models.ChoiceField(choices=num_choices)
    deep_acting_4 = models.ChoiceField(choices=num_choices)


class AffectiveCommitment(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    num_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    affective_commitment_1 = models.ChoiceField(choices=num_choices)
    affective_commitment_2 = models.ChoiceField(choices=num_choices)
    affective_commitment_3 = models.ChoiceField(choices=num_choices)
    affective_commitment_4 = models.ChoiceField(choices=num_choices)
    affective_commitment_5 = models.ChoiceField(choices=num_choices)
    affective_commitment_6 = models.ChoiceField(choices=num_choices)
    affective_commitment_7 = models.ChoiceField(choices=num_choices)
    affective_commitment_8 = models.ChoiceField(choices=num_choices)


class TaskComplexity(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    num_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    task_complexity_1 = models.ChoiceField(choices=num_choices)
    task_complexity_2 = models.ChoiceField(choices=num_choices)
    task_complexity_3 = models.ChoiceField(choices=num_choices)


class IdentificationWithLeader(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    num_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    identification_with_leader_1 = models.ChoiceField(choices=num_choices)
    identification_with_leader_2 = models.ChoiceField(choices=num_choices)
    identification_with_leader_3 = models.ChoiceField(choices=num_choices)
    identification_with_leader_4 = models.ChoiceField(choices=num_choices)
    identification_with_leader_5 = models.ChoiceField(choices=num_choices)
    identification_with_leader_6 = models.ChoiceField(choices=num_choices)


class SelfEfficacy(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    num_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    self_efficacy_1 = models.ChoiceField(choices=num_choices)
    self_efficacy_2 = models.ChoiceField(choices=num_choices)
    self_efficacy_3 = models.ChoiceField(choices=num_choices)
    self_efficacy_4 = models.ChoiceField(choices=num_choices)
    self_efficacy_5 = models.ChoiceField(choices=num_choices)
    self_efficacy_6 = models.ChoiceField(choices=num_choices)


class JobSatisfaction(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    num_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    job_satisfaction_1 = models.ChoiceField(choices=num_choices)
    job_satisfaction_2 = models.ChoiceField(choices=num_choices)
    job_satisfaction_3 = models.ChoiceField(choices=num_choices)
    job_satisfaction_4 = models.ChoiceField(choices=num_choices)
    job_satisfaction_5 = models.ChoiceField(choices=num_choices)


class WillingnessToTakeRisks(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    num_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    willingness_to_take_risks_1 = models.ChoiceField(choices=num_choices)
    willingness_to_take_risks_2 = models.ChoiceField(choices=num_choices)
    willingness_to_take_risks_3 = models.ChoiceField(choices=num_choices)
    willingness_to_take_risks_4 = models.ChoiceField(choices=num_choices)
    willingness_to_take_risks_5 = models.ChoiceField(choices=num_choices)


class Creativity(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    num_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    creativity_1 = models.ChoiceField(choices=num_choices)
    creativity_2 = models.ChoiceField(choices=num_choices)
    creativity_3 = models.ChoiceField(choices=num_choices)
    creativity_4 = models.ChoiceField(choices=num_choices)
    creativity_5 = models.ChoiceField(choices=num_choices)
    creativity_6 = models.ChoiceField(choices=num_choices)


class EmployerQuestion(models.Model):
    employ = models.ForeignKey('Polls', on_delete=models.CASCADE)
    num_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    # employer questions
    question_1 = models.ChoiceField(choices=num_choices)
    question_2 = models.ChoiceField(choices=num_choices)
    question_3 = models.ChoiceField(choices=num_choices)
    question_4 = models.ChoiceField(choices=num_choices)
    question_5 = models.ChoiceField(choices=num_choices)
    question_6 = models.ChoiceField(choices=num_choices)
    question_7 = models.ChoiceField(choices=num_choices)
    question_8 = models.ChoiceField(choices=num_choices)
    question_9 = models.ChoiceField(choices=num_choices)
    question_10 = models.ChoiceField(choices=num_choices)
    question_11 = models.ChoiceField(choices=num_choices)
    question_12 = models.ChoiceField(choices=num_choices)
    question_13 = models.ChoiceField(choices=num_choices)
    question_14 = models.ChoiceField(choices=num_choices)
    question_15 = models.ChoiceField(choices=num_choices)
    question_16 = models.ChoiceField(choices=num_choices)
    question_17 = models.ChoiceField(choices=num_choices)
    question_18 = models.ChoiceField(choices=num_choices)
    question_19 = models.ChoiceField(choices=num_choices)
    question_20 = models.ChoiceField(choices=num_choices)
