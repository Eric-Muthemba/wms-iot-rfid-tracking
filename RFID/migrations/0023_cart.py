# Generated by Django 3.1.5 on 2021-02-10 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFID', '0022_auto_20190416_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(max_length=32, unique=True)),
            ],
        ),
    ]
