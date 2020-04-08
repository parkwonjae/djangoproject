# Generated by Django 3.0.3 on 2020-04-07 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comtoemployer',
            name='company_id',
            field=models.ForeignKey(db_column='company_id', on_delete=django.db.models.deletion.CASCADE, to='polls.Company'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='company_id',
            field=models.ForeignKey(db_column='company_id', on_delete=django.db.models.deletion.CASCADE, to='polls.Company'),
        ),
        migrations.AlterField(
            model_name='selectability',
            name='company_id',
            field=models.OneToOneField(db_column='company_id', on_delete=django.db.models.deletion.CASCADE, to='polls.Company'),
        ),
    ]
