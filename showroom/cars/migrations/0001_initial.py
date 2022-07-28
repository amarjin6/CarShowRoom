# Generated by Django 4.0.6 on 2022-07-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_alter_userprofile_profile'),
        ('dealer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('last_update', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('price', models.IntegerField(default=0)),
                ('model', models.CharField(max_length=60)),
                ('amount', models.IntegerField(default=0)),
                ('dealer', models.ManyToManyField(to='dealer.dealer')),
                ('user', models.ManyToManyField(to='users.userprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarSpecifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('last_update', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('engine', models.CharField(max_length=60)),
                ('horsepower', models.IntegerField(default=0)),
                ('torque', models.IntegerField(default=0)),
                ('transmission', models.TextField()),
                ('overclocking', models.IntegerField(default=0)),
                ('car', models.ManyToManyField(to='cars.car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
