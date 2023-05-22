from django.db import models
from apps.OQC_info.models import OQC_database


# Create your models here.
class IQC_database(models.Model):
    order = models.CharField(verbose_name="订单号", max_length=13)
    gene_name = models.CharField(verbose_name="基因名称", max_length=80)
    vector_name = models.CharField(verbose_name="载体名称", max_length=100)
    titer_requirement = models.CharField(verbose_name="滴度要求", max_length=20)
    lv_DeliveryDate = models.DateTimeField(verbose_name='送检日期')
    Lot = models.CharField(verbose_name='lot号', max_length=20)
    infection_date = models.DateTimeField(verbose_name='感染日期', blank=True, null=True)
    infection_status_choice = (
        (1, '待定状态'),
        (2, '已感染(ZsGreen)'),
        (3, '已感染(Puro)'),
        (4, '已感染6孔板'),
        (5, '已感染24孔板'),
        (6, '已收集细胞，提基因组'),
        (7, '已加药，开始药筛'),
        (8, '已提RNA并反转录'),
        (9, '质检完成')
    )
    infection_status = models.SmallIntegerField(verbose_name='感染状态', choices=infection_status_choice, default=1)
    infected_people_choice = (
        (1, '吴亚楠'),
        (2, '冯邦水'),
        (3, '王梦月'),
        (4, '李井'),
        (5, '陈丛水')
    )
    infected_people = models.SmallIntegerField(verbose_name='感染人', choices=infected_people_choice, default=1)
    puro_people = models.SmallIntegerField(verbose_name='加药人', choices=infected_people_choice, default=1)
    titer_result = models.CharField(verbose_name='滴度结果', max_length=30, blank=True, null=True)
    result_choice = (
        ('待定状态', '待定状态'),
        ('质检合格', '质检合格'),
        ('质检不合格', '质检不合格')
    )
    result = models.CharField(verbose_name='质检结果', choices=result_choice, default='待定状态', max_length=10)
    Remarks = models.CharField(verbose_name='备注', max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'iqc_database'

    def save(self, *args, **kwargs):
        super(IQC_database, self).save(*args, **kwargs)
        if self.order:
            oqc_database = OQC_database(
                order=self.order,
                titer_result=self.titer_result,
                lot=self.Lot,
                lv_DeliveryDate=self.lv_DeliveryDate
            )
            oqc_database.save()



