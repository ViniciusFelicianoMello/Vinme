# Generated by Django 5.0.6 on 2024-08-13 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_content_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='section',
        ),
        migrations.AddField(
            model_name='media',
            name='content_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='blog.contentsection'),
        ),
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_type',
            field=models.CharField(max_length=50),
        ),
    ]
