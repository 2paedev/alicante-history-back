# Generated by Django 3.0 on 2019-12-17 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_auto_20191109_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.CharField(default='', max_length=10000),
        ),
    ]