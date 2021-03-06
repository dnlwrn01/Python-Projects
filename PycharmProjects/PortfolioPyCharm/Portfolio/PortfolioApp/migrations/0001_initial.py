# Generated by Django 3.2.3 on 2021-05-14 05:02

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware'), ('Project Management', 'Project Management'), ('Lifestyle', 'Lifestyle')], max_length=25)),
                ('title', models.CharField(max_length=25)),
                ('subTitle', models.CharField(max_length=25)),
                ('content', models.TextField()),
            ],
            managers=[
                ('BlogPosts', django.db.models.manager.Manager()),
            ],
        ),
    ]
