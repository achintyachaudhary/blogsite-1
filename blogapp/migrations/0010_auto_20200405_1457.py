# Generated by Django 3.0.2 on 2020-04-05 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_auto_20200404_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.AddField(
            model_name='post',
            name='post_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Post', related_query_name='Post', to='blogapp.Comment'),
        ),
    ]
