# Generated by Django 3.0.2 on 2020-04-05 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0012_auto_20200405_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_key',
            new_name='comment_key',
        ),
    ]
