# Generated by Django 3.0.2 on 2020-04-08 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_auto_20200408_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Comment', related_query_name='Commas', to='blogapp.Post'),
        ),
    ]
