# Generated by Django 3.2.7 on 2021-09-21 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_alter_schoolperiod_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledgearea',
            name='observations',
            field=models.TextField(blank=True, default='S/N', null=True, verbose_name='observaciones'),
        ),
    ]
