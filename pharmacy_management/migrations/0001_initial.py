# Generated by Django 3.2.15 on 2022-09-08 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='pharmacy_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='processing', max_length=80)),
                ('prescription', models.ImageField(blank=True, upload_to='prescription_pics')),
                ('billing_amount', models.IntegerField(default='0')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
