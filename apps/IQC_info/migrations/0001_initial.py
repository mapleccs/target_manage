# Generated by Django 4.2 on 2023-05-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IQC_database",
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
                ("order", models.CharField(max_length=13, verbose_name="订单号")),
                ("gene_name", models.CharField(max_length=80, verbose_name="基因名称")),
                ("vertor_name", models.CharField(max_length=100, verbose_name="载体名称")),
                (
                    "titer_requirement",
                    models.CharField(max_length=20, verbose_name="滴度要求"),
                ),
                ("lv_DeliveryDate", models.DateTimeField(verbose_name="送检日期")),
                ("Lot", models.CharField(max_length=20, verbose_name="lot号")),
            ],
        ),
    ]