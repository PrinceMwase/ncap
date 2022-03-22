# Generated by Django 3.2.12 on 2022-03-22 08:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ncapp', '0014_auto_20220314_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
