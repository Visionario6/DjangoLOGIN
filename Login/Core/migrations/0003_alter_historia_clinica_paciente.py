# Generated by Django 4.1.7 on 2023-02-23 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0002_remove_historia_clinica_persona_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia_clinica',
            name='Paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
