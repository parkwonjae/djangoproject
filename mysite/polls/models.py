from django.db import models
from django.contrib.auth.models import User


# Create your models here.


num_choices = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

gender_choices = (
    ('male', '남'),
    ('female', '여')
)


# company information
class Company(models.Model):
    company_id = models.CharField(max_length=15)
    company_name = models.CharField(max_length=20, blank=False)
    company_establishment = models.IntegerField(blank=False)
    company_size = models.IntegerField(blank=False)

    def __str__(self):
        return self.company_id


# employer information
class Employer(models.Model):
    employer_id = models.CharField(max_length=15)
    employer_age = models.IntegerField()
    employer_gender = models.CharField(max_length=6, choices=gender_choices)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.employer_id


class ComToEmployer(models.Model):
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE, db_column='company_id')
    employer_id = models.OneToOneField('Employer', on_delete=models.CASCADE)


# employer select abilities
class SelectAbility(models.Model):
    company_id = models.OneToOneField('Company', on_delete=models.CASCADE, db_column='company_id')
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

    def __str__(self):
        return '{} \
        compassion : {}, surface_acting: {}, deep_acting: {}, affective_commitment: {} \
        task_complexity:{}, identification_with_leader:{}, self_efficacy:{}, job_satisfaction:{} \
        willingness_to_take_risks:{}, creativity:{}'.format(
            self.company_id, self.compassion, self.surface_acting, self.deep_acting,
            self.affective_commitment, self.task_complexity, self.identification_with_leader, self.self_efficacy,
            self.job_satisfaction, self.willingness_to_take_risks, self.creativity
        )


class Compassion(models.Model):
    ability = models.ForeignKey('SelectAbility', on_delete=models.CASCADE, related_name='compassions')
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    compassion_1 = models.IntegerField(choices=num_choices)
    compassion_2 = models.IntegerField(choices=num_choices)
    compassion_3 = models.IntegerField(choices=num_choices)


class SurfaceActing(models.Model):
    ability = models.ForeignKey('SelectAbility', on_delete=models.CASCADE, related_name='surfaceactings')
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    surface_acting_1 = models.IntegerField(choices=num_choices)
    surface_acting_2 = models.IntegerField(choices=num_choices)
    surface_acting_3 = models.IntegerField(choices=num_choices)
    surface_acting_4 = models.IntegerField(choices=num_choices)
    surface_acting_5 = models.IntegerField(choices=num_choices)
    surface_acting_6 = models.IntegerField(choices=num_choices)
    surface_acting_7 = models.IntegerField(choices=num_choices)


class DeepActing(models.Model):
    ability = models.ForeignKey('SelectAbility', on_delete=models.CASCADE, related_name='deepactings')
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    deep_acting_1 = models.IntegerField(choices=num_choices)
    deep_acting_2 = models.IntegerField(choices=num_choices)
    deep_acting_3 = models.IntegerField(choices=num_choices)
    deep_acting_4 = models.IntegerField(choices=num_choices)


class AffectiveCommitment(models.Model):
    ability = models.ForeignKey('SelectAbility', on_delete=models.CASCADE, related_name='affectivecommitments')
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    affective_commitment_1 = models.IntegerField(choices=num_choices)
    affective_commitment_2 = models.IntegerField(choices=num_choices)
    affective_commitment_3 = models.IntegerField(choices=num_choices)
    affective_commitment_4 = models.IntegerField(choices=num_choices)
    affective_commitment_5 = models.IntegerField(choices=num_choices)
    affective_commitment_6 = models.IntegerField(choices=num_choices)
    affective_commitment_7 = models.IntegerField(choices=num_choices)
    affective_commitment_8 = models.IntegerField(choices=num_choices)


class TaskComplexity(models.Model):
    ability = models.ForeignKey('SelectAbility', on_delete=models.CASCADE, related_name='taskcomplexitys')
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    task_complexity_1 = models.IntegerField(choices=num_choices)
    task_complexity_2 = models.IntegerField(choices=num_choices)
    task_complexity_3 = models.IntegerField(choices=num_choices)


class IdentificationWithLeader(models.Model):
    ability = models.ForeignKey('SelectAbility', on_delete=models.CASCADE, related_name='identificationswithleaders')
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    identification_with_leader_1 = models.IntegerField(choices=num_choices)
    identification_with_leader_2 = models.IntegerField(choices=num_choices)
    identification_with_leader_3 = models.IntegerField(choices=num_choices)
    identification_with_leader_4 = models.IntegerField(choices=num_choices)
    identification_with_leader_5 = models.IntegerField(choices=num_choices)
    identification_with_leader_6 = models.IntegerField(choices=num_choices)


class SelfEfficacy(models.Model):
    ability = models.ForeignKey('SelectAbility', on_delete=models.CASCADE, related_name='selfefficacys')
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    self_efficacy_1 = models.IntegerField(choices=num_choices)
    self_efficacy_2 = models.IntegerField(choices=num_choices)
    self_efficacy_3 = models.IntegerField(choices=num_choices)
    self_efficacy_4 = models.IntegerField(choices=num_choices)
    self_efficacy_5 = models.IntegerField(choices=num_choices)
    self_efficacy_6 = models.IntegerField(choices=num_choices)


class JobSatisfaction(models.Model):
    ability = models.ForeignKey('SelectAbility', on_delete=models.CASCADE, related_name='jobsatisfactions')
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    job_satisfaction_1 = models.IntegerField(choices=num_choices)
    job_satisfaction_2 = models.IntegerField(choices=num_choices)
    job_satisfaction_3 = models.IntegerField(choices=num_choices)
    job_satisfaction_4 = models.IntegerField(choices=num_choices)
    job_satisfaction_5 = models.IntegerField(choices=num_choices)


class WillingnessToTakeRisks(models.Model):
    ability = models.ForeignKey('SelectAbility', on_delete=models.CASCADE, related_name='willingnesstotakerisks')
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    willingness_to_take_risks_1 = models.IntegerField(choices=num_choices)
    willingness_to_take_risks_2 = models.IntegerField(choices=num_choices)
    willingness_to_take_risks_3 = models.IntegerField(choices=num_choices)
    willingness_to_take_risks_4 = models.IntegerField(choices=num_choices)
    willingness_to_take_risks_5 = models.IntegerField(choices=num_choices)


class Creativity(models.Model):
    ability = models.ForeignKey('SelectAbility', on_delete=models.CASCADE, related_name='creativitys')
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    creativity_1 = models.IntegerField(choices=num_choices)
    creativity_2 = models.IntegerField(choices=num_choices)
    creativity_3 = models.IntegerField(choices=num_choices)
    creativity_4 = models.IntegerField(choices=num_choices)
    creativity_5 = models.IntegerField(choices=num_choices)
    creativity_6 = models.IntegerField(choices=num_choices)


# employer question result
class EmployerQuestion(models.Model):
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    employer_id = models.OneToOneField('Employer', on_delete=models.CASCADE)
    # employer questions
    question_1 = models.IntegerField(choices=num_choices)
    question_2 = models.IntegerField(choices=num_choices)
    question_3 = models.IntegerField(choices=num_choices)
    question_4 = models.IntegerField(choices=num_choices)
    question_5 = models.IntegerField(choices=num_choices)
    question_6 = models.IntegerField(choices=num_choices)
    question_7 = models.IntegerField(choices=num_choices)
    question_8 = models.IntegerField(choices=num_choices)
    question_9 = models.IntegerField(choices=num_choices)
    question_10 = models.IntegerField(choices=num_choices)
    question_11 = models.IntegerField(choices=num_choices)
    question_12 = models.IntegerField(choices=num_choices)
    question_13 = models.IntegerField(choices=num_choices)
    question_14 = models.IntegerField(choices=num_choices)
    question_15 = models.IntegerField(choices=num_choices)
    question_16 = models.IntegerField(choices=num_choices)
    question_17 = models.IntegerField(choices=num_choices)
    question_18 = models.IntegerField(choices=num_choices)
    question_19 = models.IntegerField(choices=num_choices)
    question_20 = models.IntegerField(choices=num_choices)
