# Generated by Django 2.1.5 on 2019-08-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='service_id',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='support',
            name='support_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
