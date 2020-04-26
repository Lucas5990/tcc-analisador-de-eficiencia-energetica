# Generated by Django 3.0.4 on 2020-04-19 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200327_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refrigerator',
            fields=[
                ('household_appliance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.HouseholdAppliance')),
                ('category', models.TextField()),
                ('refrigerator_volume', models.IntegerField()),
                ('freezer_volume', models.IntegerField()),
                ('freezer_stars', models.IntegerField()),
                ('is_frost_free', models.BooleanField()),
            ],
        ),
    ]
