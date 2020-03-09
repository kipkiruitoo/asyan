# Generated by Django 3.0.4 on 2020-03-09 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('inventory', '0008_auto_20200305_1722'),
        ('departments', '0002_auto_20200309_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('departments_name', models.CharField(max_length=40, unique=True)),
                ('warehouse_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inventory.Warehouse')),
                ('description', models.TextField(default=False)),
                ('departments_user_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.DeleteModel(
            name='departments',
        ),
    ]
