# Generated by Django 4.0.4 on 2022-04-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turf_app', '0023_turfbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='turfbooking',
            name='status',
            field=models.CharField(default='0', max_length=240, null=True),
        ),
    ]