# Generated by Django 4.2.5 on 2023-10-26 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='department',
        ),
    ]
