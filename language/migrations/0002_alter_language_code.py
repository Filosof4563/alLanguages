# Generated by Django 4.1.1 on 2022-10-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(default='en', max_length=5),
        ),
    ]