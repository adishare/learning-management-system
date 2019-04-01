
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('code', models.CharField(max_length=225)),
                ('question', models.CharField(max_length=225)),
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
            name='QuestionnaireAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('answer', models.CharField(max_length=225)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Questionnaire')),
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
            name='QuestionnaireCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=255)),
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
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('question', models.CharField(max_length=255)),
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
            name='TestimonialAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('answer', models.CharField(max_length=225)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Testimonial')),
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
            name='TestimonialCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=255)),
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
            model_name='testimonial',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.TestimonialCategory'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.Event'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.QuestionnaireCategory'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.Event'),
        ),
    ]
