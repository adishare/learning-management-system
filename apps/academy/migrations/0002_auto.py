
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competency', '0001_initial'),
        ('academy', '0001_initial'),
        ('forum', '0001_initial'),
        ('content', '0001_initial'),
        ('human_resource', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantevent',
            name='participant_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resource.Participant'),
        ),
        migrations.AddField(
            model_name='learningplan',
            name='competency_issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.StrategicPlan'),
        ),
        migrations.AddField(
            model_name='learningplan',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Location'),
        ),
        migrations.AddField(
            model_name='learningactivity',
            name='articles',
            field=models.ManyToManyField(to='content.Article'),
        ),
        migrations.AddField(
            model_name='learningactivity',
            name='competency',
            field=models.ManyToManyField(blank=True, to='competency.Competency'),
        ),
        migrations.AddField(
            model_name='learningactivity',
            name='forum',
            field=models.ManyToManyField(to='forum.Forum'),
        ),
        migrations.AddField(
            model_name='learningactivity',
            name='quiz',
            field=models.ManyToManyField(to='content.QuizQuestion'),
        ),
        migrations.AddField(
            model_name='eventplan',
            name='curriculum_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competency.Curriculum'),
        ),
        migrations.AddField(
            model_name='eventplan',
            name='learning_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.LearningPlan'),
        ),
        migrations.AddField(
            model_name='event',
            name='academy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.Academy', verbose_name='Academy'),
        ),
        migrations.AddField(
            model_name='event',
            name='curriculum_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competency.Curriculum', verbose_name='Curriculum'),
        ),
        migrations.AddField(
            model_name='event',
            name='learning_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.LearningPlan', verbose_name='Learning Plan'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Location', verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='contentcreator',
            name='academy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.Academy'),
        ),
        migrations.AddField(
            model_name='academy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Company'),
        ),
        migrations.AddField(
            model_name='academy',
            name='division',
            field=models.ManyToManyField(to='human_resource.Division'),
        ),
    ]
