# Generated by Django 2.2.13 on 2023-03-15 06:30

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_auto_20230208_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='ohshownevent',
            name='ohshown_again',
            field=models.IntegerField(blank=True, choices=[(0, '是'), (1, '否'), (2, '沒意見')], help_text='您是否希望以後有機會，或能再次看到野外的黑熊', null=True),
        ),
        migrations.AddField(
            model_name='ohshownevent',
            name='ohshown_again_reason',
            field=models.CharField(blank=True, help_text='您是否希望以後有機會，或能再次看到野外的黑熊-為什麼', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ohshownevent',
            name='prevent_ohshown_methods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, choices=[(0, '盡量結伴同行無'), (1, '必要時，沿途製造些聲響，如吹口哨、講話'), (2, '避免走夜路'), (3, '妥善收存食物、垃圾與廚餘'), (4, '看到熊在遠方時，人要輕聲離開現場'), (5, '單獨行動'), (6, '隨身攜帶哨子或鈴鐺'), (7, '攜帶防熊噴霧'), (8, '其他')], help_text='您知道以下哪些做法有助於減少遇到熊的機會，或避免不愉快地與熊相遇充', null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='ohshownevent',
            name='prevent_ohshown_methods_text_object',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='您知道以下哪些做法有助於減少遇到熊的機會，或避免不愉快地與熊相遇充-文字補充', null=True),
        ),
        migrations.AddField(
            model_name='ohshownevent',
            name='survey_if_bear_exist',
            field=models.BooleanField(blank=True, help_text='您是否會先了解您預計前往的地點有無黑熊出沒', null=True),
        ),
    ]