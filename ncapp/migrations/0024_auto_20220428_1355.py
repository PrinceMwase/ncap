# Generated by Django 3.2.12 on 2022-04-28 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ncapp', '0023_stock_support_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clinic',
            options={'ordering': ['-id'], 'verbose_name': 'Appointment'},
        ),
        migrations.AddField(
            model_name='stock',
            name='dispensation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ncapp.drugdispensation'),
            preserve_default=False,
        ),
    ]
