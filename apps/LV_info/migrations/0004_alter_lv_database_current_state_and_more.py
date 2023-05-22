# Generated by Django 4.2 on 2023-04-30 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LV_info", "0003_alter_lv_database_current_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lv_database",
            name="current_state",
            field=models.SmallIntegerField(
                choices=[(1, "转染中"), (2, "收毒中"), (3, "24小时拍照"), (4, "纯化中"), (5, "已送检")],
                verbose_name="当前状态",
            ),
        ),
        migrations.AlterField(
            model_name="lv_database",
            name="hours24_state",
            field=models.SmallIntegerField(
                choices=[(1, "正常状态"), (2, "荧光污染"), (3, "荧光效率低")],
                verbose_name="24小时订单状态",
            ),
        ),
        migrations.AlterField(
            model_name="lv_database",
            name="vertor_type",
            field=models.SmallIntegerField(
                choices=[(1, "一代载体"), (2, "二代载体"), (3, "三代载体")], verbose_name="载体类型"
            ),
        ),
    ]
