# Generated by Django 3.2.4 on 2021-06-25 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_invoice_is_paid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('-created_at',)},
        ),
    ]
