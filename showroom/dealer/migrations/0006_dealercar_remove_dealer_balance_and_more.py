# Generated by Django 4.0.6 on 2022-07-28 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_car_amount'),
        ('dealer', '0005_remove_dealer_car_remove_dealer_cars_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealerCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_dealercar', to='cars.car')),
            ],
        ),
        migrations.RemoveField(
            model_name='dealer',
            name='balance',
        ),
        migrations.DeleteModel(
            name='history_dealer_car',
        ),
        migrations.AddField(
            model_name='dealercar',
            name='dealer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dealer_dealercar', to='dealer.dealer'),
        ),
    ]
