# Generated by Django 3.1.6 on 2021-08-30 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210828_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image_2',
            field=models.ImageField(blank=True, default='portfolio/images/project-figure-main1.png', upload_to='portfolio/images/'),
        ),
    ]