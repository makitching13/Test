# Generated by Django 2.2 on 2019-04-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default='2019-01-01 00:00:00', verbose_name='date published'),
            preserve_default=False,
        ),
    ]