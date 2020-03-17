# Generated by Django 3.0.3 on 2020-03-16 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='co_id',
            new_name='company_id',
        ),
        migrations.RenameField(
            model_name='selectvariable',
            old_name='co_id',
            new_name='company_id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employee_coname',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employee_id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employee_pw',
        ),
    ]
