from django.db import models
from apps.LV_info.models import LV_database


# Create your models here.
class TechSupport_database(models.Model):
    order = models.CharField(verbose_name="订单号", max_length=20)
    order_type_choice = (
        (1, "过表达慢病毒"),
        (2, "干扰慢病毒"),
        (3, "blank"),
        (4, "sgRNA-Cas9慢病毒"),
        (5, "shRNA慢病毒"),
    )
    order_type = models.SmallIntegerField(verbose_name="订单类型", choices=order_type_choice)
    gene_name = models.CharField(verbose_name="基因名称", max_length=80)
    gene_num = models.IntegerField(verbose_name="基因大小")
    vector_name = models.CharField(verbose_name="载体名称", max_length=100)
    virus_volume = models.CharField(verbose_name='病毒量', max_length=20)
    titer_requirement = models.CharField(verbose_name="滴度要求", max_length=20)
    order_date = models.DateTimeField(verbose_name='订单日期', blank=True, null=True)
    specify_completion_date = models.DateTimeField(verbose_name='规定完成日期', blank=True, null=True)
    shipping_date = models.DateTimeField(verbose_name='发货日期', blank=True, null=True)
    customer_unit = models.CharField(verbose_name='客户单位', max_length=200)
    sales_manager = models.CharField(verbose_name='销售经理', max_length=10)
    entered_by_choice = (
        (1, '李雨晴'),
        (2, '周华香')
    )
    entered_by = models.SmallIntegerField(verbose_name='录入人', choices=entered_by_choice)
    dispatch = models.CharField(verbose_name="分装量", max_length=20)
    pipe_num = models.IntegerField(verbose_name="总支数")
    titer_result = models.CharField(verbose_name='滴度结果', blank=True, null=True, max_length=20)
    iqc_result = models.CharField(verbose_name='质检结果', blank=True, null=True, max_length=20)
    shipping_Remarks = models.CharField(verbose_name='发货备注', blank=True, null=True, max_length=300)
    Remarks = models.CharField(verbose_name='备注', max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'tech_support_database'

    def save(self, *args, **kwargs):
        super(TechSupport_database, self).save(*args, **kwargs)
        if self.order:
            lv_database = LV_database(
                order=self.order,
                order_date=self.order_date,
                order_type=self.order_type,
                gene_name=self.gene_name,
                gene_num=self.gene_num,
                vector_name=self.vector_name,
                titer_requirement=self.titer_requirement,
                dispatch=self.dispatch,
                pipe_num=self.pipe_num,
                Remarks=self.Remarks
            )
            if lv_database.current_state != 1:
                lv_database.save()
            else:
                pass

