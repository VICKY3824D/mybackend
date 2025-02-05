# Generated by Django 5.1.4 on 2025-02-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farming_v3', '0008_alter_panenan_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanaman',
            name='deskripsi',
            field=models.TextField(default='deskripsi tanaman'),
        ),
        migrations.AddField(
            model_name='tanaman',
            name='link_tanaman',
            field=models.URLField(blank=True, default='https://trans89.com/media/upload/2022/10/Tangerang-Dorong-Pasar-Besar-Sektor-Pertanian-Dengan-Budidaya-Tanaman-Pangan-Organik-653x366.jpg', null=True),
        ),
    ]
