# Generated by Django 5.0.6 on 2024-08-13 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_contentsection_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(),
        ),
    ]
