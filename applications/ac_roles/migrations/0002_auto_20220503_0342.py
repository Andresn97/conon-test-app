# Generated by Django 3.2.7 on 2022-05-03 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ac', '0010_alter_teamac_team_state'),
        ('ac_roles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performancedescriptionspokesmanac',
            name='member_ac',
        ),
        migrations.AddField(
            model_name='activitydescriptionspokesmanac',
            name='member_ac',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='member_performance_description_ac', to='ac.teamdetailac'),
            preserve_default=False,
        ),
    ]