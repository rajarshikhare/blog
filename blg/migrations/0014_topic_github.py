# Generated by Django 2.0.4 on 2018-05-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0013_auto_20180515_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='github',
            field=models.CharField(default='None', max_length=200),
        ),
    ]