# Generated by Django 4.0.2 on 2022-02-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportgroup',
            name='name',
            field=models.CharField(default=1, max_length=42),
            preserve_default=False,
        ),
    ]
