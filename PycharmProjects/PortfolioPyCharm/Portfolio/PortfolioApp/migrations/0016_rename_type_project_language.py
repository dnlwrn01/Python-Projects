# Generated by Django 3.2.3 on 2021-05-14 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0015_alter_project_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='type',
            new_name='language',
        ),
    ]
