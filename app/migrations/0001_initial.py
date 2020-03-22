# Generated by Django 3.0.4 on 2020-03-12 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseholdAppliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('energy_consumption', models.TextField(blank=True, null=True)),
                ('classification', models.CharField(max_length=1)),
                ('brand', models.TextField(blank=True, null=True)),
                ('purchased_at', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='household_appliance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voltage', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('current', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('active_power', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('energy', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('frequency', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('power_factor', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('household_appliance', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='household_appliance', to='app.HouseholdAppliance')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField()),
                ('number', models.IntegerField()),
                ('complement', models.TextField(blank=True, null=True)),
                ('neighborhood', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('energy_company', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
