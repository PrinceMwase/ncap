# Generated by Django 3.2.13 on 2022-04-20 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ncapp', '0021_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='datet',
            new_name='date',
        ),
    ]