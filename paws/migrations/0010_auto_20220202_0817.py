# Generated by Django 3.1.7 on 2022-02-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paws', '0009_auto_20220201_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='brand_logo',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.CharField(default='', max_length=100),
        ),
    ]