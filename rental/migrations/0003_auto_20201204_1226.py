# Generated by Django 3.1.3 on 2020-12-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_auto_20201204_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_dob',
            field=models.DateField(blank=True, db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Employee_dob',
            field=models.DateField(blank=True, db_index=True, max_length=200, null=True),
        ),
    ]