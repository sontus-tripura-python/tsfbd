# Generated by Django 3.1.5 on 2021-03-31 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommitteApp', '0005_auto_20210331_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchmember',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='centralmember',
            name='photo',
            field=models.ImageField(blank=True, upload_to='central'),
        ),
    ]
