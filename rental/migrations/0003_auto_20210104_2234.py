# Generated by Django 3.1.3 on 2021-01-04 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_auto_20210104_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedpropertie',
            name='property_booked',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
