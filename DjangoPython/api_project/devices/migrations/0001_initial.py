# Generated by Django 4.2.1 on 2023-06-01 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='DadoEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('data_hora', models.DateTimeField()),
                ('Dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.dispositivo')),
            ],
        ),
    ]