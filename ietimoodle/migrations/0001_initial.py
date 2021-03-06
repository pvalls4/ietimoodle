# Generated by Django 3.2 on 2022-03-10 17:34

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
            name='Centro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('localitat', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=255)),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ietimoodle.centro')),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ponderacion', models.IntegerField(default=0)),
                ('visibilidad', models.BooleanField(default=False)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ietimoodle.curso')),
            ],
        ),
        migrations.CreateModel(
            name='NivelPrivacidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ietimoodle.centro')),
                ('privacidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ietimoodle.nivelprivacidad')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsersCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suscripcion', models.BooleanField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ietimoodle.curso')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ietimoodle.user')),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField()),
                ('cualificacion', models.IntegerField(default=0)),
                ('archivo', models.FileField(upload_to='./entregas/')),
                ('fecha_entrega', models.DateTimeField(verbose_name='fecha_entrega')),
                ('comentario_profesor', models.CharField(max_length=255)),
                ('comentario_alumno', models.CharField(max_length=255)),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ietimoodle.ejercicio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ietimoodle.user')),
            ],
        ),
    ]
