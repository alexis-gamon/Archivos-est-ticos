# Generated by Django 4.1.3 on 2022-11-05 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Descripcion', models.TextField(max_length=250)),
                ('AñoLanzamiento', models.PositiveIntegerField(blank=True, null=True)),
                ('Duracion', models.PositiveIntegerField(blank=True, null=True)),
                ('Fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]