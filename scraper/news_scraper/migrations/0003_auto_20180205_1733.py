# Generated by Django 2.0.2 on 2018-02-05 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_scraper', '0002_auto_20180204_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='scanned_date',
            field=models.DateField(default=datetime.date(2018, 2, 5)),
        ),
        migrations.AlterField(
            model_name='index_value',
            name='scanned_date',
            field=models.DateField(default=datetime.date(2018, 2, 5)),
        ),
    ]
