# Generated by Django 4.2.2 on 2023-06-15 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hobbie',
            old_name='body',
            new_name='cuerpo',
        ),
        migrations.RenameField(
            model_name='hobbie',
            old_name='date',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='hobbie',
            old_name='title',
            new_name='titulo',
        ),
    ]
