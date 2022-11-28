# Generated by Django 4.1.3 on 2022-11-28 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsideTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='cost',
            new_name='change',
        ),
        migrations.AddField(
            model_name='stock',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='InsideTransection',
        ),
        migrations.AddField(
            model_name='insidetransaction',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction', to='coreAPI.stock'),
        ),
    ]
