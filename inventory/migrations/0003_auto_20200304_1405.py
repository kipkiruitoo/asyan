# Generated by Django 3.0.3 on 2020-03-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200229_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='item_description',
            field=models.TextField(default=''),
        ),
    ]
