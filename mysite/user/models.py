from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Company(models.Model):
    company_id = models.CharField(max_length=15)
    company_name = models.CharField(max_length=20, blank=False)
    company_establishment = models.IntegerField(blank=False)
    company_size = models.IntegerField(blank=False)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True)
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=True)
    data_joined = models.DateTimeField('가입일', default=timezone.now)
    employer_age = models.IntegerField()
    employer_gender = models.CharField(max_length=6, choices=(
        ('male', '남'),
        ('female', '여')
    ))
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'email' #email 사용자 식별자
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


