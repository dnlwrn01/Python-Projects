# Generated by Django 3.2.3 on 2021-05-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0021_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=' ', max_length=13),
        ),
    ]