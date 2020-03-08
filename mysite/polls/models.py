from django.db import models


# Create your models here.

# 인사담당자가 변수 선택한 테이블
class SelectVariable(models.Model):
    co_id = models.CharField(max_length=10)
    compassion = models.BooleanField(default=False)
    surface_acting = models.BooleanField(default=False)
    deep_acting = models.BooleanField(default=False)
    affective_commitment = models.BooleanField(default=False)
    task_complexity = models.BooleanField(default=False)

    def __str__(self):
        return self.co_id
