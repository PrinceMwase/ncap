# Generated by Django 3.2.12 on 2022-03-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncapp', '0015_patient_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='visit_date',
            field=models.DateField(verbose_name='Visit Date'),
        ),
        migrations.AlterField(
            model_name='drugdispensation',
            name='dis_date',
            field=models.DateField(verbose_name='Drug dispensation date'),
        ),
        migrations.AlterField(
            model_name='viralload',
            name='vl_date',
            field=models.DateField(verbose_name='viral load date'),
        ),
    ]
