# Generated by Django 3.1.6 on 2021-08-30 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='portfolio/images/project-figure-main1.png', upload_to='portfolio/images/'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image_2',
            field=models.ImageField(blank=True, default='portfolio/images/project-figure-main1.png', upload_to='portfolio/images/'),
        ),
    ]
