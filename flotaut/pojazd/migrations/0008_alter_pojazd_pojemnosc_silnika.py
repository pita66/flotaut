# Generated by Django 4.0.1 on 2022-01-17 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pojazd', '0007_alter_pojazd_ladownosc_alter_pojazd_liczba_miejsc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pojazd',
            name='pojemnosc_silnika',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
