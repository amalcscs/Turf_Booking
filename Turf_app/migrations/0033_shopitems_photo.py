# Generated by Django 4.0.4 on 2022-05-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turf_app', '0032_shopitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopitems',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
