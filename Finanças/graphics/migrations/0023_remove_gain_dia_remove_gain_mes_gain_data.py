# Generated by Django 4.1.1 on 2022-10-04 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0022_remove_gain_data_gain_dia_gain_mes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gain',
            name='dia',
        ),
        migrations.RemoveField(
            model_name='gain',
            name='mes',
        ),
        migrations.AddField(
            model_name='gain',
            name='data',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
