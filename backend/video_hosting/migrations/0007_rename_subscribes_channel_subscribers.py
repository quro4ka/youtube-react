# Generated by Django 4.1.2 on 2022-12-14 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_hosting', '0006_alter_views_options_alter_views_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='subscribes',
            new_name='subscribers',
        ),
    ]
