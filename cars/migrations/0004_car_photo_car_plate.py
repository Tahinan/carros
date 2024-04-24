# Generated by Django 5.0.2 on 2024-02-29 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_brand_alter_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
