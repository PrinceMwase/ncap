# Generated by Django 4.0.2 on 2022-02-28 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ncapp', '0007_alter_art_clinic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viralload',
            name='clinic',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ncapp.clinic'),
        ),
    ]
