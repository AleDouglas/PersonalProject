# Generated by Django 4.1.1 on 2022-10-03 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('graphics', '0004_alter_gain_usuario_alter_monthlyearnings_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gain',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
