# Generated by Django 2.0.4 on 2018-05-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0004_auto_20180518_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='algorithm_type',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='github',
            new_name='link',
        ),
        migrations.AlterField(
            model_name='topic',
            name='upload_date',
            field=models.CharField(default='Fri May 18 12:44:20 2018', max_length=50),
        ),
    ]
