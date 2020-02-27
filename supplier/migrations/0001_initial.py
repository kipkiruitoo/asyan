# Generated by Django 3.0.3 on 2020-02-26 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('registered_on', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
