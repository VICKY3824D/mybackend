# Generated by Django 5.1.4 on 2024-12-27 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farming_v3', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hama',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='pestisidapupuk',
            name='owner',
        ),
    ]