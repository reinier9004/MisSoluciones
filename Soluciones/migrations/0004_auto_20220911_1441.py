# Generated by Django 3.0.6 on 2022-09-11 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Soluciones', '0003_auto_20220826_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='mensajes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=10000)),
                ('fecha', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 11, 14, 41, 8, 436303))),
                ('usuario', models.CharField(max_length=10000)),
                ('sala', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='salas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salanombre', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RenameField(
            model_name='solucionesconcursos',
            old_name='problemaConcurso',
            new_name='solucionConcurso',
        ),
        migrations.RemoveField(
            model_name='solucionesconcursos',
            name='pagado',
        ),
    ]
