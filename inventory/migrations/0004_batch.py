# Generated by Django 3.0.3 on 2020-03-04 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_tenderapplication_discount_terms'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0003_auto_20200304_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_delivery', models.TimeField()),
                ('date_expiry', models.TimeField()),
                ('date_finished', models.TimeField()),
                ('delivered_quantity', models.IntegerField()),
                ('quantity_remaining', models.IntegerField()),
                ('state', models.CharField(choices=[('Finished', 'Finished'), ('Current', 'Current'), ('Later', 'Later')], default='Later', max_length=20)),
                ('pallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch', to='inventory.Pallet')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch', to='inventory.Products')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch', to=settings.AUTH_USER_MODEL)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch', to='supplier.Company')),
            ],
        ),
    ]
