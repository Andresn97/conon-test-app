# Generated by Django 3.2.7 on 2022-03-13 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abp_steps', '0009_auto_20220307_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemresolutionstepeightabp',
            name='image_references',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='problemresolutionstepeightabp',
            name='video_url',
            field=models.URLField(blank=True),
        ),
    ]
