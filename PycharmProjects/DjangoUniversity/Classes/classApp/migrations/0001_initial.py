# Generated by Django 3.2.2 on 2021-05-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('courseNumber', models.IntegerField(blank=True, default='000')),
                ('instructorName', models.CharField(blank=True, default='', max_length=60)),
                ('duration', models.FloatField(blank=True, default='00.0')),
            ],
        ),
    ]