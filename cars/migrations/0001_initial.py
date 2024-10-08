# Generated by Django 5.0.2 on 2024-02-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('factory_year', models.IntegerField(blank=True, null=True)),
                ('model_year', models.ImageField(blank=True, null=True, upload_to='')),
                ('value', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
