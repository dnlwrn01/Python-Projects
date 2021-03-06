# Generated by Django 3.2.3 on 2021-05-14 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0002_alter_blogpost_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='subTitle',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='type',
            field=models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware'), ('Project Management', 'Project Management'), ('Lifestyle', 'Lifestyle')], max_length=25),
        ),
    ]
