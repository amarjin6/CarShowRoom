# Generated by Django 4.0.6 on 2022-08-10 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('engine', models.CharField(max_length=60)),
                ('horsepower', models.IntegerField(default=0)),
                ('torque', models.IntegerField(default=0)),
                ('transmission', models.TextField()),
                ('overclocking', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('model', models.CharField(max_length=60)),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification_car', to='cars.carspecification')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
