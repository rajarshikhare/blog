# Generated by Django 2.0.4 on 2018-05-15 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0012_topic_data_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='data_upload',
            new_name='upload_date',
        ),
    ]
