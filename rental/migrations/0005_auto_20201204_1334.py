# Generated by Django 3.1.3 on 2020-12-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_auto_20201204_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertie',
            name='property_description',
            field=models.TextField(blank=True),
        ),
    ]
