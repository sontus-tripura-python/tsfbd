# Generated by Django 3.1.5 on 2021-03-31 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommitteApp', '0004_auto_20210328_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchmember',
            name='photo',
            field=models.ImageField(blank=True, upload_to='branchmember'),
        ),
        migrations.AlterField(
            model_name='centralmember',
            name='photo',
            field=models.ImageField(upload_to='central'),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='photo',
            field=models.ImageField(blank=True, upload_to='branchmember'),
        ),
    ]
