# Generated by Django 3.0.3 on 2020-03-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='deviceId',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
