# Generated by Django 2.1.4 on 2018-12-25 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='identification_code',
            field=models.CharField(max_length=8),
        ),
    ]
