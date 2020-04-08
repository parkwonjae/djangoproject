# Generated by Django 3.0.3 on 2020-04-07 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=15)),
                ('company_name', models.CharField(max_length=20)),
                ('company_establishment', models.IntegerField()),
                ('company_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_id', models.CharField(max_length=15)),
                ('employer_age', models.IntegerField()),
                ('employer_gender', models.CharField(choices=[('male', '남'), ('female', '여')], max_length=6)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SelectAbility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compassion', models.BooleanField(default=False)),
                ('surface_acting', models.BooleanField(default=False)),
                ('deep_acting', models.BooleanField(default=False)),
                ('affective_commitment', models.BooleanField(default=False)),
                ('task_complexity', models.BooleanField(default=False)),
                ('identification_with_leader', models.BooleanField(default=False)),
                ('self_efficacy', models.BooleanField(default=False)),
                ('job_satisfaction', models.BooleanField(default=False)),
                ('willingness_to_take_risks', models.BooleanField(default=False)),
                ('creativity', models.BooleanField(default=False)),
                ('company_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
        migrations.CreateModel(
            name='WillingnessToTakeRisks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('willingness_to_take_risks_1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('willingness_to_take_risks_2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('willingness_to_take_risks_3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('willingness_to_take_risks_4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('willingness_to_take_risks_5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='willingnesstotakerisks', to='polls.SelectAbility')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
        migrations.CreateModel(
            name='TaskComplexity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_complexity_1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('task_complexity_2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('task_complexity_3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskcomplexitys', to='polls.SelectAbility')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
        migrations.CreateModel(
            name='SurfaceActing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface_acting_1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('surface_acting_2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('surface_acting_3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('surface_acting_4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('surface_acting_5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('surface_acting_6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('surface_acting_7', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surfaceactings', to='polls.SelectAbility')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
        migrations.CreateModel(
            name='SelfEfficacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_efficacy_1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('self_efficacy_2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('self_efficacy_3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('self_efficacy_4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('self_efficacy_5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('self_efficacy_6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selfefficacys', to='polls.SelectAbility')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
        migrations.CreateModel(
            name='JobSatisfaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_satisfaction_1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('job_satisfaction_2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('job_satisfaction_3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('job_satisfaction_4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('job_satisfaction_5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobsatisfactions', to='polls.SelectAbility')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
        migrations.CreateModel(
            name='IdentificationWithLeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_with_leader_1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('identification_with_leader_2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('identification_with_leader_3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('identification_with_leader_4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('identification_with_leader_5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('identification_with_leader_6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identificationswithleaders', to='polls.SelectAbility')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_7', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_8', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_9', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_10', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_11', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_12', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_13', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_14', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_15', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_16', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_17', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_18', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_19', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question_20', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
                ('employer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Employer')),
            ],
        ),
        migrations.CreateModel(
            name='DeepActing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deep_acting_1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('deep_acting_2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('deep_acting_3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('deep_acting_4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deepactings', to='polls.SelectAbility')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Creativity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creativity_1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('creativity_2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('creativity_3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('creativity_4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('creativity_5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('creativity_6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creativitys', to='polls.SelectAbility')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
        migrations.CreateModel(
            name='ComToEmployer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
                ('employer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Employer')),
            ],
        ),
        migrations.CreateModel(
            name='Compassion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compassion_1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('compassion_2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('compassion_3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compassions', to='polls.SelectAbility')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
        migrations.CreateModel(
            name='AffectiveCommitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affective_commitment_1', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('affective_commitment_2', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('affective_commitment_3', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('affective_commitment_4', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('affective_commitment_5', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('affective_commitment_6', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('affective_commitment_7', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('affective_commitment_8', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affectivecommitments', to='polls.SelectAbility')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
    ]
