# Generated by Django 4.0.6 on 2022-07-28 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userprofile_profile'),
        ('trades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
    ]
