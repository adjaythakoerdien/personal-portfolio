# Generated by Django 3.1.6 on 2021-08-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='eind',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='intro',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='text_list',
            field=models.TextField(blank=True),
        ),
    ]