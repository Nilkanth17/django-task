# Generated by Django 5.0.3 on 2024-05-01 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_file_table_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Price',
            new_name='price',
        ),
    ]
