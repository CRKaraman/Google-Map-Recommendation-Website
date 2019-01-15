# Generated by Django 2.1.4 on 2018-12-10 12:32

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('rating', models.FloatField()),
                ('category', models.CharField(max_length=254)),
                ('descriptio', models.CharField(max_length=254)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_n', models.CharField(max_length=255)),
                ('hospital_r', models.FloatField()),
                ('contact_nu', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_nam', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('location', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='PoliceStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('police_sta', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('contact_nu', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.CharField(max_length=254)),
                ('rating', models.FloatField()),
                ('type', models.CharField(max_length=254)),
                ('cuisines', models.CharField(max_length=254)),
                ('cost', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('features', models.CharField(max_length=254)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]