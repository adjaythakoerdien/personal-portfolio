# Generated by Django 3.1.6 on 2021-08-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_project_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='uitgelicht',
            field=models.BooleanField(default=False),
        ),
    ]