# Generated by Django 4.0.4 on 2022-04-27 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=240, null=True)),
                ('Lastname', models.CharField(max_length=240, null=True)),
                ('place', models.CharField(max_length=240, null=True)),
                ('address', models.CharField(max_length=240, null=True)),
                ('pincode', models.CharField(max_length=240, null=True)),
                ('mobile', models.CharField(max_length=240, null=True)),
                ('email', models.EmailField(max_length=240, null=True)),
                ('password', models.CharField(max_length=240, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(default='', max_length=240, null=True)),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userregistrationdesignation', to='Turf_app.designation')),
            ],
        ),
    ]
