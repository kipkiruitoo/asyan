# Generated by Django 3.0.3 on 2020-03-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_head'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='img',
        ),
        migrations.RemoveField(
            model_name='user',
            name='head',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
