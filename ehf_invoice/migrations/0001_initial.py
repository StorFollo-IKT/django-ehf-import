# Generated by Django 3.1.5 on 2021-02-11 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='organisasjonsnummer')),
                ('name', models.CharField(max_length=200, verbose_name='navn')),
            ],
            options={
                'verbose_name': 'kunde',
                'verbose_name_plural': 'kunder',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=100, verbose_name='fakturanummer')),
                ('order_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='ordrenummer')),
                ('date', models.DateField(verbose_name='fakturadato')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='beløp')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ehf_invoice.customer', verbose_name='kunde')),
            ],
            options={
                'verbose_name': 'faktura',
                'verbose_name_plural': 'fakturaer',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_id', models.IntegerField(verbose_name='linje')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='beskrivelse')),
                ('name', models.CharField(max_length=300, verbose_name='navn')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='beløp')),
                ('quantity', models.IntegerField(verbose_name='antall')),
                ('sum', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='sum')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='ehf_invoice.invoice', verbose_name='faktura')),
            ],
            options={
                'verbose_name': 'fakturalinje',
                'verbose_name_plural': 'fakturalinjer',
                'ordering': ['invoice', 'line_id'],
                'unique_together': {('invoice', 'line_id')},
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='organisasjonsnummer')),
                ('name', models.CharField(max_length=200, verbose_name='navn')),
            ],
            options={
                'verbose_name': 'leverandør',
                'verbose_name_plural': 'leverandører',
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ehf_invoice.supplier', verbose_name='leverandør'),
        ),
        migrations.CreateModel(
            name='SerialNumber',
            fields=[
                ('serial', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='serienummer')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serials', to='ehf_invoice.invoiceline', verbose_name='fakturalinje')),
            ],
            options={
                'verbose_name': 'serienummer',
                'verbose_name_plural': 'serienummer',
                'unique_together': {('line', 'serial')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='invoice',
            unique_together={('supplier', 'invoice_number')},
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='invoice_attachments/%Y/')),
                ('mime', models.CharField(max_length=50, verbose_name='MIME type')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='ehf_invoice.invoice')),
            ],
            options={
                'verbose_name': 'vedlegg',
                'verbose_name_plural': 'vedlegg',
                'unique_together': {('invoice', 'name')},
            },
        ),
    ]
