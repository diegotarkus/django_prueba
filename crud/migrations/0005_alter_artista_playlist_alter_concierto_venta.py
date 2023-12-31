# Generated by Django 4.2.1 on 2023-06-28 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_alter_artista_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='playlist',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Playlist'),
        ),
        migrations.AlterField(
            model_name='concierto',
            name='venta',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Link de venta'),
        ),
    ]
