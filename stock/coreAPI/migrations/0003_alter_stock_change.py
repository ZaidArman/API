# Generated by Django 4.1.3 on 2022-11-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreAPI', '0002_insidetransaction_rename_cost_stock_change_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='change',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
