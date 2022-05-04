# Generated by Django 4.0.4 on 2022-05-04 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Turf_app', '0041_shoppayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcategory',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Shopcategorydesignation', to='Turf_app.designation'),
        ),
        migrations.AddField(
            model_name='shopitems',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Shopitemsdesignation', to='Turf_app.designation'),
        ),
    ]
