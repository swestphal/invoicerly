# Generated by Django 3.2.4 on 2021-06-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='bank_account',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
