# Generated by Django 3.2.15 on 2022-09-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy_model',
            name='prescription_text',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
