# Generated by Django 4.2 on 2023-05-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LV_info", "0012_lv_database_order_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lv_database",
            name="vector_type",
            field=models.CharField(
                choices=[("一代载体", "一代载体"), ("二代载体", "二代载体"), ("三代载体", "三代载体")],
                default="三代载体",
                max_length=10,
                verbose_name="载体类型",
            ),
        ),
    ]
