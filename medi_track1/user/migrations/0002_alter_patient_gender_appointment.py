# Generated by Django 5.0.3 on 2024-04-03 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('time', models.CharField(choices=[('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('02:00 PM', '02:00 PM'), ('02:30 PM', '02:30 PM'), ('03:00 PM', '03:00 PM'), ('03:30 PM', '03:30 PM'), ('04:00 PM', '04:00 PM'), ('04:30 PM', '04:30 PM')], max_length=10)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.doctor')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.hospital')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.patient')),
            ],
        ),
    ]
