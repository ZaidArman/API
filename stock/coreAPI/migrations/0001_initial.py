# Generated by Django 3.0.2 on 2022-11-28 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='STOCK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Valuation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_cap', models.IntegerField()),
                ('pe_ratio', models.FloatField()),
                ('stock', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='valuation', to='coreAPI.STOCK')),
            ],
        ),
        migrations.CreateModel(
            name='InsideTransection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('stock', models.ManyToManyField(related_name='Transection', to='coreAPI.STOCK')),
            ],
        ),
    ]
