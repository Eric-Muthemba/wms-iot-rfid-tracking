# Generated by Django 2.1.5 on 2019-02-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFID', '0003_auto_20190219_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]