# Generated by Django 2.1.2 on 2018-10-31 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20181031_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 19, 33, 23, 948081), verbose_name='Due'),
        ),
    ]
