# Generated by Django 4.0.6 on 2022-08-09 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('profile', models.CharField(choices=[('none', 'NONE'), ('customer', 'CUSTOMER'), ('vendor', 'VENDOR'), ('dealer', 'DEALER')], default='none', max_length=8)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfileCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_user_profile_car', to='cars.car')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user_profile_car', to='users.userprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
