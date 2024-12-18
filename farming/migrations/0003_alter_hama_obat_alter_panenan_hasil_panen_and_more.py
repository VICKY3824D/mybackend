# Generated by Django 5.1.3 on 2024-12-19 02:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farming', '0002_alter_hama_obat_alter_panenan_hasil_panen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hama',
            name='obat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='farming.pestisidapupuk'),
        ),
        migrations.AlterField(
            model_name='panenan',
            name='hasil_panen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='farming.tanaman'),
        ),
        migrations.AlterField(
            model_name='panenan',
            name='petaninya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='farming.petani'),
        ),
    ]
