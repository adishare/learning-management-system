
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competency', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('competency', models.ManyToManyField(blank=True, to='competency.Competency')),
                ('members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('proficiency', models.ManyToManyField(blank=True, to='competency.Proficiency')),
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
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='forum.Forum')),
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
            name='ThreadTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=60)),
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
            model_name='thread',
            name='tag',
            field=models.ManyToManyField(blank=True, to='forum.ThreadTag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Thread'),
        ),
    ]
