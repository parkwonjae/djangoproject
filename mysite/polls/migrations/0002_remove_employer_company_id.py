# Generated by Django 3.0.3 on 2020-04-05 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='company_id',
        ),
    ]
