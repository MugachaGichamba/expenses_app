# Generated by Django 3.2.6 on 2021-08-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='phone number'),
        ),
    ]