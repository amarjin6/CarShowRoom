# Generated by Django 4.0.6 on 2022-07-28 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarSpecifications',
            new_name='CarSpecification',
        ),
    ]
