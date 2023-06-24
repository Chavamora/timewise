# Generated by Django 4.2.2 on 2023-06-24 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0003_dairy_entry_favorito'),
    ]

    operations = [
        migrations.AddField(
            model_name='dairy_entry',
            name='mood',
            field=models.CharField(choices=[('feliz', '😊 Feliz'), ('triste', '😢 Triste'), ('enojado', '😡 Enojado'), ('sorprendido', '😮 Sorprendido'), ('confundido', '😕 Confundido')], default='enojado', max_length=20),
            preserve_default=False,
        ),
    ]
