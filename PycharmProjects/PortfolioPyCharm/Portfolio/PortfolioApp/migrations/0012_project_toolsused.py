# Generated by Django 3.2.3 on 2021-05-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0011_auto_20210514_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='toolsUsed',
            field=models.CharField(default=' ', max_length=250),
        ),
    ]
