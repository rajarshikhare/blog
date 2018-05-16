# Generated by Django 2.0.4 on 2018-05-16 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0023_auto_20180516_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 5, 16, 10, 57, 12, 408772, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='upload_date',
            field=models.CharField(default='Wed May 16 16:27:07 2018', max_length=50),
        ),
    ]
