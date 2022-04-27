# Generated by Django 4.0.4 on 2022-04-27 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Turf_app', '0002_turf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstteam', models.CharField(max_length=240, null=True)),
                ('secondteam', models.CharField(max_length=240, null=True)),
                ('result', models.CharField(max_length=240, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(default='', max_length=240, null=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='matchlocation', to='Turf_app.turf')),
                ('turf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='matchturf', to='Turf_app.turf')),
            ],
        ),
    ]