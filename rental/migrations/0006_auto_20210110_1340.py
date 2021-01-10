# Generated by Django 3.1.3 on 2021-01-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_auto_20210110_1231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property_image',
            options={'ordering': ('pro_id',), 'verbose_name': 'Property Image'},
        ),
        migrations.AlterModelOptions(
            name='property_taken',
            options={'ordering': ('customer_id',), 'verbose_name': 'Property Taken'},
        ),
        migrations.AlterField(
            model_name='propertie',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
