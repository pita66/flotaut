# Generated by Django 3.2.8 on 2022-01-11 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uzytkownik', '0002_uzytkownik_jednostka_organizacyjna'),
        ('pojazd', '0002_pojazd_masa_wlasna_alter_pojazd_numer_vin'),
        ('jednostka_organizacyjna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Karty_Paliwowe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wystawca_karty', models.CharField(max_length=45)),
                ('numer_karty', models.IntegerField()),
                ('data_waznosci_karty', models.DateField()),
                ('jednostka_organizacyjna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jednostka_organizacyjna.jednostka_organizacyjna')),
                ('pojazd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pojazd.pojazd')),
                ('uzytkownik', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uzytkownik.uzytkownik')),
            ],
        ),
    ]
