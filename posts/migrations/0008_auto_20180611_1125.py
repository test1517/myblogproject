# Generated by Django 2.0.5 on 2018-06-11 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
