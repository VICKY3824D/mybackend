# Generated by Django 5.1.4 on 2025-02-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farming_v3', '0006_remove_panenan_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='panenan',
            name='owner',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
