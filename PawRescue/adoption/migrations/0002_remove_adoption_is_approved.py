# Generated by Django 4.2.3 on 2023-07-25 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoption',
            name='is_approved',
        ),
    ]
