# Generated by Django 5.1.2 on 2024-10-29 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amrita', '0004_contact_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='names',
        ),
    ]