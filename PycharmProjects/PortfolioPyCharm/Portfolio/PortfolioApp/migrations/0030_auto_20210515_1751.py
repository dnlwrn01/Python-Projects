# Generated by Django 3.2.3 on 2021-05-15 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0029_auto_20210515_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image1',
            field=models.ImageField(upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image2',
            field=models.ImageField(upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image3',
            field=models.ImageField(upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image4',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]