from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.OQC_info.models import OQC_database
from apps.LV_info.models import LV_database


@receiver(post_save, sender=LV_database)
def update_result1(sender, instance, **kwargs):
    oqc_records = OQC_database.objects.filter(order=instance.order, lv_DeliveryDate=instance.lv_DeliveryDate)
    for record in oqc_records:
        record.vector_type = instance.vector_type
        record.save()
