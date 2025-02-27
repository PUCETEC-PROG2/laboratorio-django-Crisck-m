# Generated by Django 4.2 on 2024-12-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('A', 'Agua'), ('L', 'Lagartija'), ('F', 'Fuego'), ('T', 'Tierra'), ('E', 'Electrico'), ('P', 'PLanta')], max_length=30)),
                ('weight', models.DecimalField(decimal_places=4, max_digits=6)),
                ('height', models.DecimalField(decimal_places=4, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('level', models.IntegerField(default=1)),
            ],
        ),
    ]
