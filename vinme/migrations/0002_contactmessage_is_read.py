# Generated by Django 5.0.6 on 2024-07-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
