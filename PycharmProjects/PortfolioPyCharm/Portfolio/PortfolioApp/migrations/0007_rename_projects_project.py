# Generated by Django 3.2.3 on 2021-05-14 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0006_alter_projects_managers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
