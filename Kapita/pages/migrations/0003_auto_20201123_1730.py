# Generated by Django 3.1.3 on 2020-11-23 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_comentarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comentarios',
            new_name='Comentario',
        ),
        migrations.RenameModel(
            old_name='Publicaciones',
            new_name='Publicacione',
        ),
    ]
