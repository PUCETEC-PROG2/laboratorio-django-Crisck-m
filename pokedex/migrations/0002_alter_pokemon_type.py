# Generated by Django 4.2 on 2025-01-11 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('A', 'Agua'), ('L', 'Lagartija'), ('F', 'Fuego'), ('E', 'Electrico'), ('P', 'PLanta')], max_length=30),
        ),
    ]
