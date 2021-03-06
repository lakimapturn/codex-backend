# Generated by Django 3.1.7 on 2022-01-30 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paws', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='own_dog',
            new_name='owns_dog',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vaccinated',
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('profile_picture', models.ImageField(default='', upload_to='')),
                ('age', models.IntegerField(default=1)),
                ('breed', models.CharField(default='', max_length=100)),
                ('vaccinated', models.BooleanField(default=False)),
                ('owned_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
