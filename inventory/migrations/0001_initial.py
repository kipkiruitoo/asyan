# Generated by Django 3.0.3 on 2020-02-26 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Pallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('location', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('selling_price', models.PositiveIntegerField()),
                ('cost_price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('quantity_available', models.PositiveIntegerField(null=True)),
                ('unit_measure', models.CharField(choices=[('Kilograms', 'Kilograms'), ('Liters', 'Liters'), ('Meters', 'Meters')], max_length=20)),
                ('reoder_level', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='inventory.Category')),
                ('pallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='inventory.Pallet')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='pallet',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pallet', to='inventory.Warehouse'),
        ),
        migrations.AlterUniqueTogether(
            name='pallet',
            unique_together={('name', 'warehouse')},
        ),
    ]
