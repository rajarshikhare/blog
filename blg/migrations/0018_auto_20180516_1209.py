# Generated by Django 2.0.4 on 2018-05-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0017_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='about',
            field=models.TextField(default='Not given by the author but obviously he/she must be awesome!!s', max_length=2000),
        ),
    ]