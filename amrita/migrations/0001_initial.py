# Generated by Django 5.1.2 on 2024-10-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=1000)),
                ('father', models.CharField(max_length=1000)),
                ('mother', models.CharField(max_length=1000)),
                ('student', models.CharField(max_length=1000)),
                ('dob', models.DateField(default='2024-10-09')),
                ('addmission', models.CharField(max_length=1000)),
            ],
        ),
    ]