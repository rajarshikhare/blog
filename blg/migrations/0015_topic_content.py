# Generated by Django 2.0.4 on 2018-05-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0014_topic_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='content',
            field=models.CharField(default='None', max_length=3000),
        ),
    ]
