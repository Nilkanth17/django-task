# Generated by Django 5.0.3 on 2024-05-28 06:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_item_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 28, 12, 9, 4, 163813)),
        ),
    ]