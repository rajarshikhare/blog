# Generated by Django 2.0.4 on 2018-05-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0003_topic_abstract_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('facebook', models.CharField(max_length=300)),
                ('twitter', models.CharField(max_length=300)),
                ('instagram', models.CharField(max_length=300)),
            ],
        ),
    ]
