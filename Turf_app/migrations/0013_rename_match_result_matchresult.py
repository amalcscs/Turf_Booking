# Generated by Django 4.0.4 on 2022-04-27 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Turf_app', '0012_match_result_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='match_result',
            new_name='Matchresult',
        ),
    ]