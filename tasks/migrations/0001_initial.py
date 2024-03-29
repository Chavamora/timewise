# Generated by Django 4.2.2 on 2023-06-22 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_limite', models.DateTimeField()),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('notas', models.TextField(max_length=500)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_limite', models.DateField()),
                ('hora_comienzo', models.TimeField()),
                ('hora_limite', models.TimeField()),
                ('urgencia', models.CharField(choices=[('Urgente', 'Urgente'), ('No Urgente', 'No Urgente')], max_length=10)),
                ('importancia', models.CharField(choices=[('Importante', 'Importante'), ('No Importante', 'No Importante')], max_length=15)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('id_lista', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='tasks.tasklist')),
            ],
        ),
    ]
