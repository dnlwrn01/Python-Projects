# Generated by Django 3.2.3 on 2021-05-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0033_alter_project_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image1',
            field=models.ImageField(upload_to='Portfolio/static/img/upload/'),
        ),
    ]
