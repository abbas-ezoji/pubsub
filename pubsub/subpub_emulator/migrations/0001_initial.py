# Generated by Django 3.2.7 on 2021-09-04 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('device_id', models.CharField(max_length=60, verbose_name='DeviceId')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
            ],
            options={
                'verbose_name_plural': 'Device',
            },
        ),
    ]
