# Generated by Django 4.1.7 on 2023-04-01 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_patien_email_booking_patient_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
