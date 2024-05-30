# Generated by Django 5.0.3 on 2024-05-11 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_item_created_at_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 11, 11, 40, 5, 236053)),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
    ]