# Generated by Django 5.0.2 on 2024-04-17 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_car_bio_alter_car_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, default='cars/default.jpg', null=True, upload_to='cars/'),
        ),
    ]
