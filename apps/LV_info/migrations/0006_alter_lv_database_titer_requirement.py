# Generated by Django 4.2 on 2023-05-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LV_info", "0005_alter_lv_database_current_state_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lv_database",
            name="titer_requirement",
            field=models.CharField(max_length=20, verbose_name="滴度要求"),
        ),
    ]
