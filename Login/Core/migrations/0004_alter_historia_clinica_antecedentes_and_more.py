# Generated by Django 4.1.7 on 2023-02-23 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0003_alter_historia_clinica_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia_clinica',
            name='Antecedentes',
            field=models.TextField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='Diagnostico',
            field=models.TextField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='Epicrisis',
            field=models.TextField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='Paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='Recomendaciones',
            field=models.TextField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='Tratamientos',
            field=models.TextField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]