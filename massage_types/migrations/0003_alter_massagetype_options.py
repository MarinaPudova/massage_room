# Generated by Django 5.0.3 on 2024-03-15 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('massage_types', '0002_massagetype_current_status_massagetype_massage_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='massagetype',
            options={'ordering': ('name',)},
        ),
    ]
