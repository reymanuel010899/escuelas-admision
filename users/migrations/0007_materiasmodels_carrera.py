# Generated by Django 4.2 on 2023-06-11 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_materiasmodels_semestre'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiasmodels',
            name='carrera',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='carrera_materia_reverce', to='users.carrerasmodels'),
            preserve_default=False,
        ),
    ]
