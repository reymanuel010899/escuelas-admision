# Generated by Django 4.2 on 2023-06-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_materiasmodels_credito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escuelasmodels',
            name='nombre',
            field=models.CharField(max_length=80),
        ),
    ]
