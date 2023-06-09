# Generated by Django 4.2 on 2023-05-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OQC_database",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.CharField(max_length=20, verbose_name="订单号")),
                ("lot", models.CharField(max_length=10, verbose_name="lot号")),
                ("titer_result", models.CharField(max_length=20, verbose_name="滴度结果")),
                (
                    "shopping_Remarks",
                    models.CharField(max_length=300, verbose_name="发货备注"),
                ),
            ],
        ),
    ]
