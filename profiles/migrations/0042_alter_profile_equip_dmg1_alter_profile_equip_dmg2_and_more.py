# Generated by Django 4.1.3 on 2024-01-16 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0041_profile_equip_armor_profile_equip_attacks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='equip_dmg1',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='equip_dmg2',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='equip_hp',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
