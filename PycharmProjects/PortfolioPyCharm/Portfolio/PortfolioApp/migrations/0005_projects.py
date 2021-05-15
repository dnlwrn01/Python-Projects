# Generated by Django 3.2.3 on 2021-05-14 05:42

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0004_auto_20210514_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('type', models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware'), ('Project Management', 'Project Management'), ('Lifestyle', 'Lifestyle')], max_length=25)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('subTitle', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
            managers=[
                ('BlogPosts', django.db.models.manager.Manager()),
            ],
        ),
    ]