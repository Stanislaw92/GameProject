# Generated by Django 4.1.3 on 2023-10-22 19:03

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0022_remove_combat1v1_result_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='combat1v1_result',
            name='result1',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
