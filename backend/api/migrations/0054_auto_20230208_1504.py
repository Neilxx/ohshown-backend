# Generated by Django 2.2.13 on 2023-02-08 07:04

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_auto_20230111_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shownform',
            name='bear_behavior_text',
        ),
        migrations.RemoveField(
            model_name='shownform',
            name='bear_reaction_text',
        ),
        migrations.RemoveField(
            model_name='shownform',
            name='food_object',
        ),
        migrations.RemoveField(
            model_name='shownform',
            name='human_behavior_text',
        ),
        migrations.RemoveField(
            model_name='shownform',
            name='human_reaction_text',
        ),
        migrations.AddField(
            model_name='shownform',
            name='bear_behavior_text_object',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='目擊當下熊在做什麼-文字補充', null=True),
        ),
        migrations.AddField(
            model_name='shownform',
            name='bear_reaction_text_object',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='黑熊發現目擊者後，黑熊的反應-文字補充', null=True),
        ),
        migrations.AddField(
            model_name='shownform',
            name='food_text_object',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='黑熊在吃什麼-文字補充', null=True),
        ),
        migrations.AddField(
            model_name='shownform',
            name='human_behavior_text_object',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='目擊當下目擊者在做什麼-文字補充', null=True),
        ),
        migrations.AddField(
            model_name='shownform',
            name='human_reaction_text_object',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='目擊黑熊後，目擊者反應-文字補充', null=True),
        ),
    ]