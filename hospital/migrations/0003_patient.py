# Generated by Django 4.2.5 on 2023-10-26 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_doctor_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('symptoms', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images/')),
                ('status', models.BooleanField(default=False)),
                ('assignedDoctorId', models.PositiveIntegerField(null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
