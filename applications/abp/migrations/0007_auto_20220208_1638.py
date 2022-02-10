# Generated by Django 3.2.7 on 2022-02-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0006_alter_rubricdetailabp_grade_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubricabp',
            name='abp_final_value',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rubricdetailabp',
            name='grade_percentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rubricdetailabp',
            name='rating_value',
            field=models.FloatField(default=0),
        ),
    ]