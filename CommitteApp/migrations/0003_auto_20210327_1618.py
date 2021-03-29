# Generated by Django 3.1.5 on 2021-03-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommitteApp', '0002_auto_20210327_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centralmember',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='centralmember',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='central'),
        ),
        migrations.AlterField(
            model_name='centralmember',
            name='position',
            field=models.CharField(max_length=50),
        ),
    ]
