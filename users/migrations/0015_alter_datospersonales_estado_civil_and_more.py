# Generated by Django 4.2 on 2023-06-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_escuelasmodels_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datospersonales',
            name='estado_civil',
            field=models.CharField(choices=[('s', 'SOLTERO'), ('c', 'CASADO'), ('u', 'UNION LIBRE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='datossiesmilitar',
            name='idiomas_dominas',
            field=models.CharField(choices=[('español', 'ESPAÑOL'), ('ingles', 'INGLES'), ('otros', 'OTROS')], max_length=10),
        ),
    ]
