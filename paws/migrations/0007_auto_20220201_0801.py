# Generated by Django 3.1.7 on 2022-02-01 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paws', '0006_auto_20220131_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='response',
            field=models.TextField(default=''),
        ),
    ]
