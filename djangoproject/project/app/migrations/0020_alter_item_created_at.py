# Generated by Django 5.0.3 on 2024-05-28 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_user_login_ragister_alter_item_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 28, 11, 37, 3, 804248)),
        ),
    ]
