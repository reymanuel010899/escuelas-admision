# Generated by Django 4.2.1 on 2023-05-10 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_secionmodels_estudiante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secionmodels',
            name='estudiante',
            field=models.ManyToManyField(blank=True, null=True, related_name='estudiante_secion_reverce', to='users.estudiantesmodels'),
        ),
    ]
