# Generated by Django 3.1.6 on 2021-08-24 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210227_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaardigheid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vaardigheden', models.CharField(max_length=250)),
            ],
        ),
    ]
