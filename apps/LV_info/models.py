from django.db import models
from apps.IQC_info.models import IQC_database


# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class LV_database(models.Model):
    order = models.CharField(verbose_name="订单号", max_length=13)
    order_type_choice = (
        (1, "过表达慢病毒"),
        (2, "干扰慢病毒"),
        (3, "blank"),
        (4, "sgRNA-Cas9慢病毒"),
        (5, "shRNA慢病毒"),
    )
    order_type = models.SmallIntegerField(verbose_name="订单类型", choices=order_type_choice)
    order_date = models.DateTimeField(verbose_name="下单日期", blank=True, null=True)
    gene_name = models.CharField(verbose_name="基因名称", max_length=80)
    gene_num = models.IntegerField(verbose_name="基因大小")
    vector_name = models.CharField(verbose_name="载体名称", max_length=100)
    titer_requirement = models.CharField(verbose_name="滴度要求", max_length=20)
    dispatch = models.CharField(verbose_name="分装量", max_length=20)
    pipe_num = models.IntegerField(verbose_name="总支数")
    vector_type_choice = (
        ('一代载体', '一代载体'),
        ('二代载体', '二代载体'),
        ('三代载体', '三代载体')
    )
    vector_type = models.CharField(verbose_name='载体类型', choices=vector_type_choice, default='三代载体', max_length=10)
    plasmid_ReceiptDate = models.DateTimeField(verbose_name='质粒接收日期', blank=True, null=True)
    transfection_date = models.DateTimeField(verbose_name='转染完成日期', blank=True, null=True)
    hours24_state_choice = (
        (1, '待定状态'),
        (2, '正常状态'),
        (3, '荧光污染'),
        (4, '荧光效率低')
    )
    hours24_state = models.SmallIntegerField(verbose_name='24小时订单状态', choices=hours24_state_choice, default=1)
    lv_CollectDate = models.DateTimeField(verbose_name='收毒日期', blank=True, null=True)
    lv_RurificationDate = models.DateTimeField(verbose_name='纯化日期', blank=True, null=True)
    lv_DeliveryDate = models.DateTimeField(verbose_name='送检日期', blank=True, null=True)
    current_state_choice = (
        (1, '待定状态'),
        (2, '转染中'),
        (3, '24小时拍照'),
        (4, '收毒中'),
        (5, '纯化中'),
        (6, '已送检')
    )
    current_state = models.SmallIntegerField(verbose_name='当前状态', choices=current_state_choice, default=1)
    Remarks = models.CharField(verbose_name='备注', max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'lv_database'

    def create_lot(self):
        lv_DeliveryDate = self.lv_DeliveryDate
        year = lv_DeliveryDate.year
        month = lv_DeliveryDate.month
        day = lv_DeliveryDate.day
        lot = 'V1'+str(year+10)[2:4]+str(month+20)+str(day+30)
        return lot

    def save(self, *args, **kwargs):
        super(LV_database, self).save(*args, **kwargs)
        if self.current_state == 6:
            lot = self.create_lot()
            iqc_database = IQC_database(
                order=self.order,
                gene_name=self.gene_name,
                vector_name=self.vector_name,
                titer_requirement=self.titer_requirement,
                lv_DeliveryDate=self.lv_DeliveryDate,
                Lot=lot,
                Remarks=self.Remarks,
            )
            iqc_database.save()

