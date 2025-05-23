# Generated by Django 4.1.3 on 2024-01-16 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_item_base_type_of_wep'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_base',
            name='stat1',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_base',
            name='stat2',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_base',
            name='stat3',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_base',
            name='stat4',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_base',
            name='stat5',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_prefix',
            name='stat1',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_prefix',
            name='stat2',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_prefix',
            name='stat3',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_prefix',
            name='stat4',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_prefix',
            name='stat5',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_sufix',
            name='stat1',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_sufix',
            name='stat2',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_sufix',
            name='stat3',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_sufix',
            name='stat4',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_sufix',
            name='stat5',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
