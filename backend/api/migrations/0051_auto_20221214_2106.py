# Generated by Django 2.2.13 on 2022-12-14 13:06

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_auto_20221120_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shownform',
            name='food_object',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]