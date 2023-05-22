from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.OQC_info.models import OQC_database
from apps.TechSupport_info.models import TechSupport_database


@receiver(post_save, sender=TechSupport_database)
def update_result1(sender, instance, **kwargs):
    oqc_records = OQC_database.objects.filter(order=instance.order)
    for record in oqc_records:
        record.dispatch = instance.dispatch
        record.pipe_num = instance.pipe_num
        record.save()
