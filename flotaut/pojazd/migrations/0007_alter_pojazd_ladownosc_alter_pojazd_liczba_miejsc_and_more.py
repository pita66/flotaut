# Generated by Django 4.0.1 on 2022-01-17 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pojazd', '0006_alter_pojazd_data_pierwszej_rejestracji_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pojazd',
            name='ladownosc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pojazd',
            name='liczba_miejsc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pojazd',
            name='masa_calkowita',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pojazd',
            name='moc_silnika',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
