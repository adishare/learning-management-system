
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('cycle', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('format', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
                ('content_type', models.IntegerField()),
                ('objid', models.CharField(max_length=255)),
            ],
        ),
    ]
