# Generated by Django 4.0.6 on 2022-07-28 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_dealer_alter_car_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='dealer',
        ),
        migrations.RemoveField(
            model_name='car',
            name='user',
        ),
    ]
