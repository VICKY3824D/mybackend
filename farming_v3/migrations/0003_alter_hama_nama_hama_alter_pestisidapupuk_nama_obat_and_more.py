# Generated by Django 5.1.4 on 2024-12-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farming_v3', '0002_remove_hama_owner_remove_pestisidapupuk_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hama',
            name='nama_hama',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='pestisidapupuk',
            name='nama_obat',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tanaman',
            name='nama_tanaman',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
