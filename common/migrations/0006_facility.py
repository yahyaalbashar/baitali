# Generated by Django 4.0.4 on 2023-02-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=255)),
            ],
        ),
    ]
