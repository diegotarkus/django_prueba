# Generated by Django 4.2.1 on 2023-06-28 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='playlist',
            field=models.URLField(blank=True, null=True, verbose_name='Playlist'),
        ),
    ]
