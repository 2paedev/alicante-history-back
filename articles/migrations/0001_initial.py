# Generated by Django 3.0 on 2020-01-11 23:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_image', '0001_initial'),
        ('authors', '0001_initial'),
        ('tags', '0001_initial'),
        ('bibliography', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('text', models.CharField(default='', max_length=10000)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_author', to='authors.Author')),
                ('bibliography', models.ManyToManyField(to='bibliography.Bibliography')),
                ('images', models.ManyToManyField(to='custom_image.CustomImage')),
                ('tags', models.ManyToManyField(to='tags.Tag')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
