# Generated by Django 4.0.4 on 2023-03-08 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_facility'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='mobile',
            new_name='email',
        ),
    ]
