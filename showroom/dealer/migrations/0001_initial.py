# Generated by Django 4.0.6 on 2022-07-28 20:35

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('last_update', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('name', models.CharField(max_length=30)),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('history', models.TextField(default='')),
                ('profile', models.ManyToManyField(blank=True, to='users.userprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DealerCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('last_update', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('amount', models.IntegerField(default=0)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_dealer_car', to='cars.car')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dealer_dealer_car', to='dealer.dealer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
