# Generated by Django 4.1.3 on 2023-10-27 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0032_alter_textmessage_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textmessage',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='msg_sender', to='profiles.profile'),
        ),
    ]
