# Generated by Django 5.0.3 on 2024-04-04 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_department_and_hospital_doctor_hospital_department_and'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='hospital_department_and',
            new_name='hospital_and_department',
        ),
    ]
