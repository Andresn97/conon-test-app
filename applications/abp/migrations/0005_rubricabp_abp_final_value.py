# Generated by Django 3.2.7 on 2022-01-31 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0004_auto_20220127_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubricabp',
            name='abp_final_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
