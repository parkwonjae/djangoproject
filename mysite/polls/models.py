from django.db import models


# Create your models here.

# 인사담당자가 변수 선택한 테이블
class SelectVariable(models.Model):
    company_id = models.CharField(max_length=10)
    compassion = models.BooleanField(default=False)
    surface_acting = models.BooleanField(default=False)
    deep_acting = models.BooleanField(default=False)
    affective_commitment = models.BooleanField(default=False)
    task_complexity = models.BooleanField(default=False)

    def __str__(self):
        return self.company_id


class Employee(models.Model):
    company_id = models.CharField(max_length=10)
    compassion_1 = models.IntegerField(null=True)
    compassion_2 = models.IntegerField(null=True)
    surface_acting_1 = models.IntegerField(null=True)
    surface_acting_2 = models.IntegerField(null=True)
    deep_acting_1 = models.IntegerField(null=True)
    deep_acting_2 = models.IntegerField(null=True)
    affective_commitment_1 = models.IntegerField(null=True)
    affective_commitment_2 = models.IntegerField(null=True)
    task_complexity_1 = models.IntegerField(null=True)
    task_complexity_2 = models.IntegerField(null=True)

    def __str__(self):
        return self.company_id
