from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.IQC_info.models import IQC_database
from apps.TechSupport_info.models import TechSupport_database


@receiver(post_save, sender=IQC_database)
def update_result1(sender, instance, **kwargs):
    techsupport_records = TechSupport_database.objects.filter(order=instance.order)
    for record in techsupport_records:
        record.titer_result = instance.titer_result
        record.iqc_result = instance.result
        record.save()

