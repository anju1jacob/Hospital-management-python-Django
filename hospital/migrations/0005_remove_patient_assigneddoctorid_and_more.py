# Generated by Django 4.2.5 on 2023-10-27 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_remove_patient_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='assignedDoctorId',
        ),
        migrations.AddField(
            model_name='patient',
            name='assignedDoctor',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
