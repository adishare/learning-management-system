
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
            name='LearningFocus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('unit_business', models.CharField(max_length=225)),
                ('year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], default=2019)),
                ('org_competence', models.CharField(max_length=225)),
                ('objective', models.CharField(max_length=225)),
                ('staff', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('manager', models.CharField(max_length=225)),
                ('senior_manager', models.CharField(max_length=225)),
                ('top_management', models.CharField(max_length=225)),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.Academy')),
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
    ]