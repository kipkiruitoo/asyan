# Generated by Django 3.0.3 on 2020-03-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200304_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='head',
            field=models.BooleanField(default=False),
        ),
    ]
