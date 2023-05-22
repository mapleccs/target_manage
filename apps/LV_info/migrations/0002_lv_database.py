# Generated by Django 4.2 on 2023-04-30 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LV_info", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LV_database",
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
                (
                    "order_type",
                    models.SmallIntegerField(
                        choices=[
                            (1, "过表达慢病毒"),
                            (2, "干扰慢病毒"),
                            (3, "blank"),
                            (4, "sgRNA-Cas9慢病毒"),
                            (5, "shRNA慢病毒"),
                        ],
                        verbose_name="订单类型",
                    ),
                ),
                ("gene_name", models.CharField(max_length=80, verbose_name="基因名称")),
                ("gene_num", models.IntegerField(verbose_name="基因大小")),
                ("vertor_name", models.CharField(max_length=100, verbose_name="载体名称")),
                ("titer_requirement", models.BigIntegerField(verbose_name="滴度要求")),
                ("dispatch", models.IntegerField(verbose_name="分装量")),
                ("pipe_num", models.IntegerField(verbose_name="总支数")),
                (
                    "vertor_type",
                    models.SmallIntegerField(
                        choices=[(1, "一代载体"), (2, "二代载体"), (3, "三代载体")],
                        default=3,
                        verbose_name="载体类型",
                    ),
                ),
                (
                    "plasmid_ReceiptDate",
                    models.DateTimeField(blank=True, null=True, verbose_name="质粒接收日期"),
                ),
                (
                    "transfection_date",
                    models.DateTimeField(blank=True, null=True, verbose_name="转染完成日期"),
                ),
                (
                    "hours24_state",
                    models.SmallIntegerField(
                        choices=[(1, "正常状态"), (2, "荧光污染"), (3, "荧光效率低")],
                        default=1,
                        verbose_name="24小时订单状态",
                    ),
                ),
                (
                    "lv_CollectDate",
                    models.DateTimeField(blank=True, null=True, verbose_name="收毒日期"),
                ),
                (
                    "lv_RurificationDate",
                    models.DateTimeField(blank=True, null=True, verbose_name="纯化日期"),
                ),
                (
                    "lv_DeliveryDate",
                    models.DateTimeField(blank=True, null=True, verbose_name="送检日期"),
                ),
                (
                    "current_state",
                    models.SmallIntegerField(
                        choices=[
                            (1, "转染中"),
                            (2, "收毒中"),
                            (3, "24小时拍照"),
                            (4, "纯化中"),
                            (5, "已送检"),
                        ],
                        default=1,
                    ),
                ),
            ],
        ),
    ]
