# Generated by Django 3.2.12 on 2022-04-11 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ncapp', '0018_auto_20220408_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='art',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]