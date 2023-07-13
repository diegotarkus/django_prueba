# Generated by Django 4.2.1 on 2023-07-10 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'ordering': ['correo'],
            },
        ),
        migrations.AlterModelOptions(
            name='datoscontacto',
            options={'ordering': ['id'], 'verbose_name': 'contacto', 'verbose_name_plural': 'contactos'},
        ),
    ]
