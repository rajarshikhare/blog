# Generated by Django 2.0.4 on 2018-05-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0006_auto_20180519_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitedetail',
            name='sitemap',
            field=models.TextField(default='None', max_length=10000),
        ),
        migrations.AlterField(
            model_name='topic',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='upload_date',
            field=models.CharField(default='Wed May 23 06:56:52 2018', max_length=50),
        ),
    ]
