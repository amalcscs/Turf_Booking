# Generated by Django 4.0.2 on 2022-07-28 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Turf_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turfbooking',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TurfBookingowner', to='Turf_app.user_registration'),
        ),
    ]
