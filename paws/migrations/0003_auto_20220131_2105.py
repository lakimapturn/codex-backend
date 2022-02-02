# Generated by Django 3.1.7 on 2022-01-31 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paws', '0002_auto_20220130_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='owned_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='owns_dog',
        ),
        migrations.AddField(
            model_name='user',
            name='dog_owned',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='paws.dog'),
        ),
    ]
