# Generated by Django 5.0.12 on 2025-04-07 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constancias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constancia',
            name='horaInscripcion',
        ),
        migrations.AlterField(
            model_name='constancia',
            name='fechaInscripcion',
            field=models.DateTimeField(),
        ),
    ]
