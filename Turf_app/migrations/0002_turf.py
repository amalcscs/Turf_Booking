# Generated by Django 4.0.4 on 2022-04-27 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Turf_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Turfname', models.CharField(max_length=240, null=True)),
                ('location', models.CharField(max_length=240, null=True)),
                ('sport', models.CharField(max_length=240, null=True)),
                ('capacity', models.CharField(max_length=240, null=True)),
                ('Price', models.CharField(max_length=240, null=True)),
                ('amenties', models.CharField(max_length=240, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(default='', max_length=240, null=True)),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='turfdesignation', to='Turf_app.designation')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='turfuser', to='Turf_app.user_registration')),
            ],
        ),
    ]