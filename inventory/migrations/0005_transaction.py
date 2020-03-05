# Generated by Django 3.0.3 on 2020-03-05 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0004_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='inventory.Batch')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='inventory.Products')),
                ('sold_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
