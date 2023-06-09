# Generated by Django 4.2 on 2023-05-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("IQC_info", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="iqc_database",
            name="Remarks",
            field=models.CharField(
                blank=True, max_length=300, null=True, verbose_name="备注"
            ),
        ),
        migrations.AddField(
            model_name="iqc_database",
            name="infection_date",
            field=models.DateTimeField(blank=True, null=True, verbose_name="感染日期"),
        ),
        migrations.AddField(
            model_name="iqc_database",
            name="infection_status",
            field=models.SmallIntegerField(
                choices=[
                    (1, "待定状态"),
                    (2, "已感染(ZsGreen)"),
                    (3, "已感染(Puro)"),
                    (4, "已感染6孔板"),
                    (5, "已感染24孔板"),
                    (6, "已收集细胞，提基因组"),
                    (7, "已加药，开始药筛"),
                    (8, "已提RNA并反转录"),
                ],
                default=1,
                verbose_name="感染状态",
            ),
        ),
        migrations.AddField(
            model_name="iqc_database",
            name="result",
            field=models.SmallIntegerField(
                choices=[(1, "待定状态"), (2, "质检合格"), (3, "质检不合格")],
                default=1,
                verbose_name="质检结果",
            ),
        ),
        migrations.AddField(
            model_name="iqc_database",
            name="titer_result",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="滴度结果"
            ),
        ),
    ]
