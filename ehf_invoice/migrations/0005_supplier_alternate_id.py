# Generated by Django 3.1.8 on 2021-12-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ehf_invoice', '0004_mime_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='alternate_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True,
                                   verbose_name='organisasjonsnummer (ikke numerisk)'),
        ),
    ]
