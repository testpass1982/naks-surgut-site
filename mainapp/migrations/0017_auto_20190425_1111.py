# Generated by Django 2.1.5 on 2019-04-25 11:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20190425_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profstandard',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 25, 11, 11, 52, 637768, tzinfo=utc)),
        ),
    ]