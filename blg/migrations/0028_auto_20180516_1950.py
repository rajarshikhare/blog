# Generated by Django 2.0.4 on 2018-05-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0027_auto_20180516_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='websitedetail',
            old_name='about_website',
            new_name='about',
        ),
        migrations.AlterField(
            model_name='topic',
            name='upload_date',
            field=models.CharField(default='Wed May 16 19:50:53 2018', max_length=50),
        ),
    ]
