# Generated by Django 3.1.3 on 2021-01-04 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0002_auto_20210104_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='Rwandan_franc',
            new_name='Rwandan',
        ),
        migrations.RenameField(
            model_name='rate',
            old_name='congolese_franc',
            new_name='congolese',
        ),
    ]