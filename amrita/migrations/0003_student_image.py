# Generated by Django 5.1.2 on 2024-10-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amrita', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='h', upload_to='static'),
        ),
    ]
