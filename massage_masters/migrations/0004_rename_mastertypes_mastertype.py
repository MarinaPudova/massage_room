# Generated by Django 5.0.2 on 2024-02-18 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('massage_masters', '0003_mastertypes_massagemaster_master_types'),
        ('massage_types', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MasterTypes',
            new_name='MasterType',
        ),
    ]