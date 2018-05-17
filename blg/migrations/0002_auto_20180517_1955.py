# Generated by Django 2.0.4 on 2018-05-17 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blg.Author'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='upload_date',
            field=models.CharField(default='Thu May 17 19:55:01 2018', max_length=50),
        ),
    ]
