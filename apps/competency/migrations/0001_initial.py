
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('human_resource', '0001_initial'),
        ('academy', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('title', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Company')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competency.Competency')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
                'abstract': False,
                'base_manager_name': 'data',
                'default_manager_name': 'data',
            },
            managers=[
                ('data', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CompetencyRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Company')),
                ('competency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competency.Competency')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.Position')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
                'abstract': False,
                'base_manager_name': 'data',
                'default_manager_name': 'data',
            },
            managers=[
                ('data', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('title', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField()),
                ('claim', models.CharField(choices=[('N', 'Not Claimmed'), ('C', 'Claimmed')], max_length=2)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Company')),
                ('competency_goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competency.Competency')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.StrategicPlan')),
                ('learning_activity', models.ManyToManyField(blank=True, related_name='learning_activity', to='academy.LearningActivity')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
                'abstract': False,
                'base_manager_name': 'data',
                'default_manager_name': 'data',
            },
            managers=[
                ('data', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCompetency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Company')),
                ('competency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competency.Competency')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.Employee')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
                'abstract': False,
                'base_manager_name': 'data',
                'default_manager_name': 'data',
            },
            managers=[
                ('data', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Proficiency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('level', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=1, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Company')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
                'abstract': False,
                'base_manager_name': 'data',
                'default_manager_name': 'data',
            },
            managers=[
                ('data', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='employeecompetency',
            name='proficiency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competency.Proficiency'),
        ),
        migrations.AddField(
            model_name='competencyrequirement',
            name='proficiency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competency.Proficiency'),
        ),
    ]
