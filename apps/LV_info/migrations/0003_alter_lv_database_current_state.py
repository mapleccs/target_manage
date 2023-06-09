# Generated by Django 4.2 on 2023-04-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LV_info", "0002_lv_database"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lv_database",
            name="current_state",
            field=models.SmallIntegerField(
                choices=[(1, "转染中"), (2, "收毒中"), (3, "24小时拍照"), (4, "纯化中"), (5, "已送检")],
                default=1,
                verbose_name="当前状态",
            ),
        ),
    ]
