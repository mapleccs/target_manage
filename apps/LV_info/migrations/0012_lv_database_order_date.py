# Generated by Django 4.2 on 2023-05-17 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LV_info", "0011_alter_lv_database_vector_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="lv_database",
            name="order_date",
            field=models.DateTimeField(default="2022-01-01", verbose_name="下单日期"),
        ),
    ]
