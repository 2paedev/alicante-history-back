# Generated by Django 2.2.7 on 2019-11-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
