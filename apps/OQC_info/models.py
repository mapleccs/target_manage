from django.db import models


# Create your models here.
class OQC_database(models.Model):
    order = models.CharField(verbose_name='订单号', max_length=20)
    lv_DeliveryDate = models.DateTimeField(verbose_name='送检日期', blank=True, null=True)
    gene_name = models.CharField(verbose_name="基因名称", max_length=80, blank=True, null=True)
    vector_name = models.CharField(verbose_name="载体名称", max_length=100, blank=True, null=True)
    vector_type = models.CharField(verbose_name='载体类型', blank=True, null=True, max_length=10)
    lot = models.CharField(verbose_name='lot号', max_length=10)
    titer_result = models.CharField(verbose_name='滴度结果', max_length=20, blank=True,
                                    null=True)  # 这里需要注意下，理论上该值不能为空值，但是不设置为空值，会报错
    dispatch = models.CharField(verbose_name="分装量", max_length=20, blank=True, null=True)
    pipe_num = models.IntegerField(verbose_name="总支数", blank=True, null=True)
    reporter_choice = (
        ('吴亚楠', '吴亚楠'),
        ('冯邦水', '冯邦水'),
        ('陈丛水', '陈丛水')
    )
    reporter = models.CharField(verbose_name='报告人', choices=reporter_choice, default='吴亚楠', max_length=10)
    report_date = models.DateTimeField(verbose_name='报告日期', blank=True, null=True)
    checker = models.CharField(verbose_name='审核人', choices=reporter_choice, default='吴亚楠', max_length=10)
    check_date = models.DateTimeField(verbose_name='审核日期', blank=True, null=True)
    shopping_Remarks = models.CharField(verbose_name='发货备注', max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'oqc_database'
