# Generated by Django 5.1.2 on 2024-10-29 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amrita', '0009_rename_suggest_suggests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggests',
            name='mobiles',
        ),
    ]